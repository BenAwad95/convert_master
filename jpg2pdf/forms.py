from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_jpg(value):
    if not value.name.endswith('.jpg'):
        raise ValidationError(_('The file must jpg image!.'), params={'value': value})

class JpgForm(forms.Form):
    image_jpg = forms.FileField(help_text='Select Image with extension "jpg"', validators=[validate_jpg])