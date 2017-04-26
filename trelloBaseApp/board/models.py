from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# from django.core.urlresolvers import reverse

@python_2_unicode_compatible
class Board(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=600)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class task(models.Model):
    board               =       models.ForeignKey(Board,on_delete=models.CASCADE)
    task_name           =       models.CharField(max_length=55)
    def __str__(self):
        return  self.task_name

@python_2_unicode_compatible
class card(models.Model):
    tasks = models.ForeignKey(task, on_delete=models.CASCADE)
    card_name = models.CharField(max_length=55,null=True)
    Comments   = models.CharField(max_length=200)
    def __str__(self):
        return self.card_name

# Create your models here.
