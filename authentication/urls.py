from rest_framework_simplejwt.views import TokenBlacklistView, TokenObtainPairView
from django.urls import path
from . import views


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='signup'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
]