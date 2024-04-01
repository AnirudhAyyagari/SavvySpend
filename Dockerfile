# Use the official Python image as a base image
FROM python:3.10-slim-bullseye

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/requirements.txt

COPY *.py /app/

# Install Vim and the Python dependencies
RUN apt-get update && apt-get install -y vim \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
