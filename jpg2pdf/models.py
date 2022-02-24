from django.db import models


class Jpg2Pdf(models.Model):
    image = models.FileField(upload_to='jpg_images/')
