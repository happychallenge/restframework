from django.db import models

# Create your models here.
class Game(models.Model):
    """docstring for Game"""
    """ 설명 """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30)
    released_dt = models.DateTimeField()
    category = models.CharField(max_length=200, blank=True, default='')
    played = models.BooleanField(default=False)

    class Meta:
        ordering = ('name', )
        
    def __str__(self):
        return self.name

    