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

#region author-urls #ToDO
    # path('tutor/courses/', auth_views.UserRegistrationView.as_view(), name='register'),
    # path('tutor/performance/', auth_views.UserRegistrationView.as_view(), name='register'),
    # path('tutor/content/', auth_views.UserRegistrationView.as_view(), name='register'),
    # path('tutor/reviews/', auth_views.UserRegistrationView.as_view(), name='register'),
#endregion

# region user-urls #ToDo
    # path('user/courses/', auth_views.UserRegistrationView.as_view(), name='register'),
    # path('user/enrollments/', auth_views.UserRegistrationView.as_view(), name='register'),
    # path('user/progress/', auth_views.UserRegistrationView.as_view(), name='register'),
    # path('user/cart/', auth_views.UserRegistrationView.as_view(), name='register'),
    # path('user/favorites/', auth_views.UserRegistrationView.as_view(), name='register'),
#endregion

]