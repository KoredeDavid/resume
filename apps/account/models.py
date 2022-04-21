from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model



from .validators import username_validator, username_min_length

# Create your models here.


class CustomUser(AbstractUser):
    is_cleaned = False

    username = models.CharField(
        _('username'),
        max_length=30,
        help_text=_('Letters, digits and underscore only.'),
        unique=True,
        validators=[username_validator, username_min_length],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), unique=True)

    def clean(self):
        if self.username:
            UserModel = get_user_model()
            query_username = UserModel.objects.filter(username__iexact=self.username).first()

            if query_username:
                if self.id != query_username.id:
                    raise ValidationError({'username': 'A user with that username already exists.'})

        self.is_cleaned = True

    def save(self, *args, **kwargs):
        if not self.is_cleaned:
            self.full_clean()

        super().save(*args, **kwargs)

