from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from pymongo import MongoClient
from django.conf import settings

class TaskCreateView(APIView):
    def post(self, request):
        # Validate and create the task
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "message": "Task created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "failure",
            "message": "Validation failed",
            "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class TaskListView(APIView):
    def get(self, request):
        tasks = Task.objects.all()  # Get all tasks
        serializer = TaskSerializer(tasks, many=True)
        return Response({
            "status": "success",
            "message": "Tasks retrieved successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

class TaskRetrieveView(APIView):
    def get(self, request, task_id):
        try:
            task = Task.objects.get(task_id=task_id)  # Get task by ID
            serializer = TaskSerializer(task)
            return Response({
                "status": "success",
                "message": "Task retrieved successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({
                "status": "failure",
                "message": f"Task with ID '{task_id}' not found",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)

class TaskUpdateView(APIView):
    def put(self, request, task_id):
        try:
            task = Task.objects.get(task_id=task_id)  # Get task by ID
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": "success",
                    "message": "Task updated successfully",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
            return Response({
                "status": "failure",
                "message": "Validation failed",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response({
                "status": "failure",
                "message": f"Task with ID '{task_id}' not found",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)

class TaskDeleteView(APIView):
    def delete(self, request, task_id):
        client = MongoClient(settings.MONGO_DB_URI)
        db = client["Task_management"]
        task_collection = db["tasks"]
        task = task_collection.find_one({"task_id": task_id})
        
        if not task:
            return Response({
                "status": "failure",
                "message": f"Task with task_id '{task_id}' not found.",
                "data": {}
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Delete the task from the database
        task_collection.delete_one({"task_id": task_id})
        
        return Response({
            "status": "success",
            "message": f"Task with task_id '{task_id}' deleted successfully.",
            "data": {}
        }, status=status.HTTP_200_OK)