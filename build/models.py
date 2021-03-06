from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Script(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    snippet = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=1000, null=True, blank=True)
    code = models.TextField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title