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
    full_name = CharField('ФИО', max_length=200)
    external = BooleanField('Внешний пользователь', default=False)
    is_active = BooleanField('Active', default=False)
    is_admin = BooleanField('Admin', default=False)
    is_superuser = BooleanField('Superuser', default=False)
    user_permissions = ManyToManyField(Permission, verbose_name='Разрешения', blank=True)
    groups = ManyToManyField(Group, verbose_name='Группы', blank=True)
    last_login = DateTimeField('Последняя активность', auto_now=True)
    date_create = DateTimeField('Дата добавления', auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name: str = 'пользователь'
        verbose_name_plural: str = 'пользователи'

    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, obj=None) -> bool:
        """ Есть ли у пользователя конкретное разрешение? """
        return True

    def has_module_perms(self, app_label) -> bool:
        """ Есть ли у пользователя права на просмотр приложения app_label? """
        return True

    @property
    def is_staff(self) -> bool:
        """ Сотрудник админ? """
        return self.is_admin

    def save(self, *args, **kwargs):
        full_name = self.full_name.lower()
        if full_name is ['root', 'администратор', 'admin']:
            return status.HTTP_401_UNAUTHORIZED
        else:
            super().save(*args, **kwargs)
