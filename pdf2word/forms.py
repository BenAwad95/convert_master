from django import forms

class Pdf2wordForm(forms.Form):
    pdf_file = forms.FileField(help_text='Select pdf file')

