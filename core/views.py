from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth.views import LoginView as DjangoLV

from .forms import CustomAuthenticationForm, CustomUserCreationForm
from .models import UserModel


class HomePageView(TemplateView):
    template_name = 'index.html'


class RegistrationView(CreateView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = 'login/'
    model = UserModel


class LoginView(DjangoLV):
    template_name = 'registration/login.html'
    form_class = CustomAuthenticationForm
    success_url = 'dashboard/'


class FeatureView(TemplateView):
    template_name = 'features.html'


class HelpView(TemplateView):
    template_name = 'help.html'