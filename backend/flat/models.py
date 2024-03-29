from django.db import models

class Flat(models.Model):
    title = models.CharField(max_length=255)
    image = models.URLField()
    
    def __str__(self) -> str:
        return self.title