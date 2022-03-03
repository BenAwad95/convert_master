from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms



def validate_jpg(value):
    if not value.name.endswith('.jpg'):
        raise ValidationError(_('The file must jpg image!.'), params={'value': value})
class Pdf2jpgForm(forms.Form):
    pdf_file = forms.FileField(help_text='Select pdf file.')