from rest_framework import serializers
from .models import Task  # Assuming you have a Task model

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['task_id', 'status', 'description', 'created_at', 'updated_at']
