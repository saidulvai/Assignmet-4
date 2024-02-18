from django.db import models
from TaskCategory.models import Category
# Create your models here.
class Task_Model(models.Model):
    task_title = models.CharField(max_length=100)
    task_description = models.TextField()
    is_complete = models.BooleanField(default=False)
    task_assigned_date = models.DateField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.task_title