from django.db import models

# Create your models here.
class CariclumVitae(models.Model):
    cv = models.FileField(upload_to="cv")