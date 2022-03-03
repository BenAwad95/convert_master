from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms


def validate_jpg(value):
    if not value.name.endswith('.docx'):
        raise ValidationError(_('The file must docx!.'), params={'value': value})
class Word2pdfForm(forms.Form):
    docx_file = forms.FileField(help_text='Select docs file.')

