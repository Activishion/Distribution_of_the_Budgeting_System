from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, Permission, Group
from django.db.models import (CharField, BooleanField, DateTimeField,
    TextField, EmailField, ManyToManyField)
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
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser):
    email = EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True
    )
    name = CharField('Имя', max_length=100)
    external = BooleanField(default=False)
    is_active = BooleanField(default=False)
    is_admin = BooleanField(default=False)
    is_superuser = BooleanField(default=False)
    user_permissions = ManyToManyField(Permission, blank=True)
    groups = ManyToManyField(Group, blank=True)
    last_login = DateTimeField(auto_now=True)

    """ Create """
    date_create = DateTimeField('Дата добавления', auto_now_add=True)
    added_via_portal = BooleanField('Добавлено через портал', default=True)

    """ Moderation """
    moderator_is_decision = BooleanField('Проверка модератора', default=False)
    moderator = CharField('Модератор', max_length=100, blank=True, null=True)
    data_moderation = DateTimeField('Дата модерации', blank=True, null=True)
    comment = TextField('Комментарий модератора', blank=True, null=True)

    """ Delete """
    date_delete = DateTimeField('Дата удаления', blank=True, null=True)
    comment_delete = TextField('Комментарий при удалении', blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name: str = 'пользователь'
        verbose_name_plural: str = 'пользователи'

    def __str__(self) -> str:
        return self.name

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
        name = self.name.lower()
        if name is ['root', 'администратор', 'admin']:
            return status.HTTP_401_UNAUTHORIZED
        else:
            super().save(*args, **kwargs)
