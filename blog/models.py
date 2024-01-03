from django.db import models

class Blog(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    description = models.TextField()
    data = models.DateField()


    def __str__(self):
        return self.title