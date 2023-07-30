from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .tasks import send_message

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(_("e-mail address"), unique=True)
    cpf = models.CharField(_("CPF"), max_length=11, blank=True, null=True)
    telefone = models.CharField(_("Phone"), max_length=11, blank=True, null=True)
    data_nascimento = models.DateField(
        _("Birth Date"), auto_now=False, auto_now_add=False, blank=True, null=True
    )
    password_reset_token_created = models.DateTimeField(null=True, blank=True)


    
    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    EMAIL_FIELD = "email"


    def __str__(self):
        return self.email

@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        message = {
            "username": instance.username,
            "email": instance.email,
            "password": instance.password,
            "type": "create"
        }
        send_message.delay(message)

@receiver(post_delete, sender=User)
def delete_user(sender, instance, **kwargs):
    message = {
        "username": instance.username,
        "email": instance.email,
        "type": "delete"
    }
    send_message.delay(message)