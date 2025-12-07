from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class taskmodel(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    is_del = models.BooleanField(default=False)
    is_comp = models.BooleanField(default=False)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
