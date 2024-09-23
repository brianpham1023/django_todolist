from django.db import models

# Create your models here.
class todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank= True, null = True)
    is_done = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add= True)
