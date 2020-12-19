from django.db import models


class Websites(models.Model):
    """
    Represents a website
    """
    name = models.CharField(max_length=100)
    URL = models.URLField()

    def __str__(self):
        return self.name
