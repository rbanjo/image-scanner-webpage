# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

# Create your models here.
class date(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True)
