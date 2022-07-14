from django.db import models
from django.contrib.auth.models import UserManager,  AbstractUser


class CustomUser(UserManager):

    use_in_migrations = True

    def _create_user(self, email, password=None, **extra_fields):  
        if not email:
            raise ValueError("The email cannot be empty")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.activation_code = user.generate_activation_code()
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=8)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUser()

    def __str__(self) -> str:
        return self.email



    def generate_activation_code(self):
        from django.utils.crypto import get_random_string
        code = get_random_string(8)
        return code

    class Meta:
        app_label = 'users'