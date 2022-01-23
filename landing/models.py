from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Token(models.Model):
#     name = models.CharField(max_length=2000, null=True)
#     value = models.TextField(null=True)

#     def __str__(self):
#         return f"{self.name} ({self.value[:20]})"  


class Token(models.Model):
    name = models.CharField(max_length=1000, null=True)
    value = models.TextField(null=True)

    def __str__(self):
        return f"{self.name} ({self.value[:20]})"