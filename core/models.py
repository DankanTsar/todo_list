from django.db import models

# Create your models here.

class ToDoItem(models.Model):
    app_label = 'task_list'
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title