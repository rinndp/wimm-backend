from django.urls import path

from users import views
from users.views import LoginView
from users.views.register import RegisterView

urlpatterns = [
    path("users/login", LoginView.as_view(), name="login"),
    path("users/register", RegisterView.as_view(), name="register"),
]