from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    labels = {
        'complete': 'Check if completed'
    }

    def __str__(self):
        return self.title
