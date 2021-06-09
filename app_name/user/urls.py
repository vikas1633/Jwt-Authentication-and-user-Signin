from django.conf.urls import url
from app_name.user.views import UserRegistrationView


urlpatterns = [
    url('signup', UserRegistrationView.as_view()),
    ]






    
    