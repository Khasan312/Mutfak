from doctest import FAIL_FAST
from .models import User
from main.celery import app
from django.core.mail import send_mail

def set_activaion_code(user):
    code = user.generate_activaion_code()
    if User.objects.filter(activation_code=code).exists():
        user.set_activation_code()
    else:
        user.activation_code = code
        user.save()


@app.task
def send_activation_email(email, activation_code):
    activation_url = f'http://localhost:8000/user/activate/{activation_code}/'

    message = f'''thank for your signing up
                follow this link {activation_url}'''


    send_mail(
        'Heey boy',
        message,
        'test@mail.ru',
        [email,],
        fail_silently=False
    )