from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, Permission, Group
from django.db.models import (CharField, BooleanField, DateTimeField,
    EmailField, ManyToManyField)
from rest_framework import status


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser):
    email = EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True
    )
    full_name = CharField('Full_name', max_length=200)
    external_user = BooleanField('External_user', default=False)
    is_active = BooleanField('Active', default=False)
    is_admin = BooleanField('Admin', default=False)
    is_superuser = BooleanField('Superuser', default=False)
    user_permissions = ManyToManyField(Permission, verbose_name='Permissions', blank=True)
    groups = ManyToManyField(Group, verbose_name='Groups', blank=True)
    last_login = DateTimeField('Last_active', auto_now=True)
    date_create = DateTimeField('Date_of_creation', auto_now_add=True)

    news_subscription = BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name: str = 'user'
        verbose_name_plural: str = 'users'

    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, obj=None) -> bool:
        """ Does the user have specific permission? """
        return True

    def has_module_perms(self, app_label) -> bool:
        """ Does the user have permission to view the application app_label? """
        return True

    @property
    def is_staff(self) -> bool:
        """ Employee admin? """
        return self.is_admin

    def save(self, *args, **kwargs):
        full_name = self.full_name.lower()
        if full_name is ['root', 'администратор', 'admin']:
            return status.HTTP_401_UNAUTHORIZED
        else:
            super().save(*args, **kwargs)
