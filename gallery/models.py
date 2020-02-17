from django.db import models

class Painting(models.Model):
    title = models.CharField(max_length = 155)
    description = models.CharField(max_length = 255)
    image = models.URLField()

    def __str__(self):
        return self.title

# Create your models here.
