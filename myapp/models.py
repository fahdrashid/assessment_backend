from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)  # Title of the todo item

    def __str__(self):
        return self.title