from django.conf.urls import url
from .views import UserProfileView


urlpatterns = [
    url('profile', UserProfileView.as_view()),
]