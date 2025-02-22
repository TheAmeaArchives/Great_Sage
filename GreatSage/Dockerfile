# Use the official Python image as base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download the english model for spacy
RUN python -m spacy download en_core_web_md

# Copy the Django app into the container
COPY . .

# Expose the port Django will run on
EXPOSE 8000

# Start the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]