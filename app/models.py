from django.db import models

# Create your models here.


class Db_finder(models.Model):

    url = models.CharField(max_length=100,unique=True)
    keyword = models.TextField()

    def __str__(self):
        return self.url