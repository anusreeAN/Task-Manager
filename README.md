# Task Manager API

A RESTful API for managing tasks, built using **Django REST Framework** with **MongoDB** as the backend. It supports full CRUD operations, input validation, and structured JSON responses — ideal for task-tracking applications or backend integrations.

## Features

- Task CRUD (Create, Read, Update, Delete)
- RESTful endpoints using Django REST Framework
- MongoDB integration using `pymongo`
- Error handling and validation
- Modular codebase structure (Django apps)

## Tech Stack

- Backend: Django, Django REST Framework
- Database: MongoDB
- Language: Python 3.10+
- Tools: Git, VS Code

## API Endpoints

| Method | Endpoint                          | Description            |
|--------|-----------------------------------|------------------------|
| GET    | `/api/tasks/`                     | List all tasks         |
| POST   | `/api/tasks/`                     | Create a new task      |
| GET    | `/api/tasks/<task_id>/`           | Retrieve a task        |
| PUT    | `/api/tasks/<task_id>/update/`    | Update a task          |
| DELETE | `/api/tasks/<task_id>/delete/`    | Delete a task          |

## Sample JSON

**Create Task**

```json
{
  "task_id": "task_001",
  "title": "Buy groceries",
  "description": "Milk, Bread, Eggs",
  "status": "Pending"
}
