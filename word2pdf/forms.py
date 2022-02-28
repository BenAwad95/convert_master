from django import forms


class Word2pdfForm(forms.Form):
    docx_file = forms.FileField(help_text='Select docs file.')

