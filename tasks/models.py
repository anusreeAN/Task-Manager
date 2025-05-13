from djongo import models 

class Task(models.Model):
    task_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tasks' 

    def __str__(self):
        return self.task_id
