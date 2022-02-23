from django import forms


class JpgForm(forms.Form):
    image_jpg = forms.FileField(help_text='Select Image with extension "jpg"')