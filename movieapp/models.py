from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)  # A string field
    description = models.TextField()  # A text field for longer content
    is_active = models.BooleanField()

    def __str__(self):
        return self.title