from authentication import views as auth_views
from authentication import views as auth_views
from django.urls import path, register_converter, re_path
# from authentication.models import User
from course.utils import FourDigitYear
from . import views
app_name = 'core'



register_converter(FourDigitYear, 'fourdigit')
urlpatterns = [
    # path( 'archive/<fourdigit:year>/<int:month>/<int:day>',article),
    # re_path(r"archive/(?P<year>[0-9]{2,4})/"),

    path('userprofile/', auth_views.UserProfileView.as_view(), name='userprofile'),
    path('register/', auth_views.UserRegistrationView.as_view(), name='register'),

# region admin-urls
    # path('admin/approvals/', auth_views.UserRegistrationView.as_view(), name='register'),
    # path('admin/reports/', auth_views.UserRegistrationView.as_view(), name='register'),
    # path('admin/content-moderation/', auth_views.UserRegistrationView.as_view(), name='register'),
#endregion



]