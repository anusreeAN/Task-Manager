# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container at /usr/src/app
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# # Run migrations, collect static files, and start the application
# RUN python manage.py makemigrations
# RUN python manage.py migrate

# Add this to your Dockerfile to install wait-for-it
RUN apt-get update && apt-get install -y wait-for-it

CMD ["gunicorn", "--bind", "0.0.0.0:8001", "task_management.wsgi:application"]
