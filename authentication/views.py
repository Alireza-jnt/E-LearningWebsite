# from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter, OpenApiResponse
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import UserSerializer, UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.models import update_last_login
# from drf_spectacular.types import OpenApiTypes
# from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import generics, status
# from rest_framework.views import APIView
# from authentication.models import *
# from django.http import request
from django.urls import reverse
from .models import User
# from drf_spectacular.utils import (
#     extend_schema,
#     OpenApiParameter,
#     OpenApiExample,
# )



# Create your views here.

class UserProfileView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user = request.user

        # Customize the response based on the user's role
        if user.role != 3:
            # Return all fields for role 2
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif user.role == 3:
            # Return limited fields for role 3
            limited_data = {
                "username": user.username,
                "name": user.first_name,
                "family": user.last_name,
                "phone_number": user.phone_number,  # Assuming phone_number exists in the User model
                "email": user.email,
            }
            return Response(limited_data, status=status.HTTP_200_OK)
        else:
            # Handle other roles or invalid role IDs
            return Response(
                {"detail": "Access denied for your role."},
                status=status.HTTP_403_FORBIDDEN
            )

class LogoutView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    #region schema
    # @extend_schema(
    #     summary="Log Out User",
    #     description=(
    #         "Logs out the user by blacklisting the provided refresh token. "
    #         "The user must be authenticated, and the `Authorization` header must include a valid access token in the format: `Bearer <access_token>`. "
    #         "In the request body, provide the refresh token as `{ \"refresh\": \"<refresh_token>\" }`."
    #     ),
    #     request={
    #         "application/json": {
    #             "type": "object",
    #             "properties": {
    #                 "refresh": {
    #                     "type": "string",
    #                     "description": "The refresh token to be blacklisted for logout.",
    #                 },
    #             },
    #             "required": ["refresh"],
    #         }
    #     },
    #     parameters=[
    #         OpenApiParameter(
    #             name="Authorization",
    #             location=OpenApiParameter.HEADER,
    #             description="Bearer <access_token>",
    #             required=True,
    #             type=OpenApiTypes.STR,
    #         ),
    #     ],
    #     responses={
    #         205: OpenApiResponse(
    #             response={
    #                 "type": "object",
    #                 "properties": {
    #                     "message": {
    #                         "type": "string",
    #                         "example": "Successfully logged out",
    #                     },
    #                 },
    #             },
    #             description="Successfully logged out.",
    #         ),
    #         400: OpenApiResponse(
    #             response={
    #                 "type": "object",
    #                 "properties": {
    #                     "error": {
    #                         "type": "string",
    #                         "example": "Refresh token is required",
    #                     },
    #                 },
    #             },
    #             description="Error occurred during logout.",
    #         ),
    #     },
    #     examples=[
    #         OpenApiExample(
    #             "Request Example",
    #             summary="Sample Request",
    #             description="This is how the request body should look.",
    #             value={"refresh": "<refresh_token>"},
    #             request_only=True,
    #         ),
    #         OpenApiExample(
    #             "Success Response",
    #             summary="Successful Logout",
    #             description="This is the response when logout is successful.",
    #             value={"message": "Successfully logged out"},
    #             response_only=True,
    #         ),
    #         OpenApiExample(
    #             "Error Response",
    #             summary="Error Case",
    #             description="This is the response when the refresh token is invalid or missing.",
    #             value={"error": "Refresh token is required"},
    #             response_only=True,
    #         ),
    #     ],
    # )
    #endregion
    def create(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response(
                    {"error": "Refresh token is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"message": "Successfully logged out"},
                status=status.HTTP_205_RESET_CONTENT,
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()  # Required to avoid AssertionError
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return Response(
            {"detail": "Method 'GET' not allowed."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {
                "message": "Registration successful. Please log in.",
                "login_url": reverse('login')  # Adjust 'login' to match your login view name
            },
            status=status.HTTP_201_CREATED
        )


# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = TokenObtainPairSerializer
#
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         try:
#             # Retrieve the user from the serializer context
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             user = serializer.user
#
#             # Update the last_login field
#             update_last_login(None, user)
#         except Exception as e:
#             return Response({"detail": "An error occurred while updating last_login."},
#                             status=status.HTTP_400_BAD_REQUEST)
#
#         return response
#