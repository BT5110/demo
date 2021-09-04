from django.db import models


# Create your models here.
class Greeting(models.Model):
    id = models.AutoField(primary_key=True)
    when = models.DateTimeField("date created", auto_now_add=True)
