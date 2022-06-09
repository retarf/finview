from django.db import models

class Period(models.Model):
    name = models.CharField(primary_key=True, max_length=7)