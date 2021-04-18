from django.db import models


class src(models.Model):
    logo_border = models.CharField(max_length=200)
    dominant_color = models.CharField(max_length=200)
