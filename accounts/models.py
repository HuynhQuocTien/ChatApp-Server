from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        extra_fields.setdefault('username', email)  # Đặt username thành email
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_super(self, email, password, **extra_field):
    #     extra_field.setdefault('is_staff', True)
    #     extra_field.setdefault('is_superuser', True)
    #     return self.create_user(email, password, **extra_field)

    def create_super(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


# class User(AbstractUser,PermissionsMixin):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=255, blank=True)
#     last_name = models.CharField(max_length=255, blank=True)
#     is_active=models.BooleanField(default=True)
#     is_staff=models.BooleanField(default=False)
#     date_joined=models.DateTimeField(auto_now_add=True)

class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=False, blank=True, null=True)  # Cho phép username trống
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self) -> str:
        return self.email
