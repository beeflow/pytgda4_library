from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, FormView

from user.forms import RegisterUserForm
from user.models import User


class RegisterUserView(CreateView):
    template_name = "user/register.html"
    model = User
    form_class = RegisterUserForm

    def get_success_url(self):
        return reverse("index")


class LoginView(FormView):
    template_name = "user/register.html"
    form_class = AuthenticationForm

    def get_success_url(self):
        messages.info(self.request, "Siemanizator :P")
        return reverse("index")