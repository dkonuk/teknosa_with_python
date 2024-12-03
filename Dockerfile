# Use an official Python runtime as the base image
FROM python:3.9

# Set the label for the author
LABEL authors="denizkonuk"

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV SE_OFFLINE=false

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the project files into the container
COPY . .

# Set the entrypoint command to run the tests
CMD ["pytest", "tests"]