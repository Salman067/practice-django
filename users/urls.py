from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.Register.as_view()),
    path('login/',views.LoginView.as_view()),
    path('user/',views.UserView.as_view()),  # Endpoint to get user's details
    path('logout/',views.LogOutView.as_view()),  # Endpoint to log out user
]
