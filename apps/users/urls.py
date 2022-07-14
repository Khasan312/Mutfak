from django.urls import path
from users.views import ActivateView, RegistrationView, UserAPIView, LoginView

urlpatterns = [
    path('users/', UserAPIView.as_view()),
    path('register/', RegistrationView.as_view()),
    path('activate/<str:activation_code>/', ActivateView.as_view()),
    path('login/', LoginView.as_view()),

]