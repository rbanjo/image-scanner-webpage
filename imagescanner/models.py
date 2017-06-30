# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class date(models.Model):
    date = models.DateTimeField(default = datetime.now, blank = true)
