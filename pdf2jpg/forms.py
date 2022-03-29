from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms



def validate_pdf(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError(_('The file must pdf!.'), params={'value': value})
class Pdf2jpgForm(forms.Form):
    pdf_file = forms.FileField(help_text='Select pdf file.', validators=[validate_pdf])