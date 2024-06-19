# Use the official lightweight Python image
FROM python:3.10-alpine

# Set the working directory in the container
WORKDIR /app

# Install system dependencies and Python build dependencies
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    openssl-dev \
    postgresql-dev \
    && pip install --upgrade pip

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Specify the command to run the application
CMD ["python3", "app.py"]
