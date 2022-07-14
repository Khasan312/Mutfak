from django.urls import path
from apps.users.views import LoginView

from food.views import HelpView

urlpatterns = [
    path('v1/', HelpView.as_view()),
]