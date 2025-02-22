from authentication import views as auth_views
from authentication import views as auth_views
from django.urls import path
from authentication.models import User
from . import views
app_name = 'core'


urlpatterns = [

    path('userprofile/', auth_views.UserProfileView.as_view(), name='userprofile'),
    path('register/', auth_views.UserRegistrationView.as_view(), name='register'),

# region admin-urls
    # path('admin/approvals/', auth_views.UserRegistrationView.as_view(), name='register'),
    # path('admin/reports/', auth_views.UserRegistrationView.as_view(), name='register'),
    # path('admin/content-moderation/', auth_views.UserRegistrationView.as_view(), name='register'),
#endregion



]