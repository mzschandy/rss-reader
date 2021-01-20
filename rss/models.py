from django.db import models
from picklefield.fields import PickledObjectField

# Create your models here.
class FeedList(models.Model):
    name = models.CharField(max_length=250)
    feed = PickledObjectField()


    def __str__(self):
        return self.name