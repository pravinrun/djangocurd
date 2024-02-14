from django.db import models

class dhote(models.Model):
    name=models.CharField(max_length=20)
    gmail=models.CharField(max_length=20)
    mobile=models.IntegerField(null=True)
    date=models.CharField(max_length=20)
# Create your models here.
