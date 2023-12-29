from django.urls import path, include
from . import  views

urlpatterns = [
    path('register/', views.RegistrationView.as_view(),  name='register'),
    path('login/', views.LoginView.as_view(), name = 'login'),
    path('features/', views.FeatureView.as_view(), name='features'),
    path('help/', views.HelpView.as_view(), name='help'),
    path('', views.HomePageView.as_view(), name='index'),
    path('', include('django.contrib.auth.urls')),
]