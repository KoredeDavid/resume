from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinLengthValidator, RegexValidator

from . import models

username_validator = RegexValidator(regex=r'^[\w]+\Z', message=_('Enter a valid username. Your name should only '
                                                                 'letters, numbers and underscore.'), flags=0, )
username_min_length = MinLengthValidator(5)


