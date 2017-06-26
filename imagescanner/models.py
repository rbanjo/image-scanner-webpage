from django.db import models

# Create your models here.

class upload(models.Model):
   file_name = models.CharField(max_length = 300, default = 'resume')
   first_name = models.CharField(max_length = 500, default = 'John')
   last_name = models.CharField(max_length = 200, default = 'smith')
   email_address = models.CharField(max_length = 700, default = 'example@gmail.com') 
   
   def __str__(self):
      return self.file_name + ' - ' + self.last_name
   
