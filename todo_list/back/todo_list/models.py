from django.db import models

class List(models.Model):
    text = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text
