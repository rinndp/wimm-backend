from django.urls import path

from users import views
from users.views import LoginView

urlpatterns = [
    path("users/login", LoginView.as_view(), name="login"),
]