from rest_framework_simplejwt.views import TokenBlacklistView, TokenObtainPairView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, UserRegistrationView

router = DefaultRouter()
router.register(r'profile', UserProfileViewSet, basename='profile')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='signup'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='register'),
]
