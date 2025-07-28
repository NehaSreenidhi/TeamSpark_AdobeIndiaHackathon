# Use slim Python image and target amd64 platform
FROM --platform=linux/amd64 python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements.txt early for better caching
COPY requirements.txt .

# Install system and Python dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir pymupdf

# Copy all project files into /app
COPY . .

# Ensure input/output folders exist (for local bind mount)
RUN mkdir -p input output

# Set default command
CMD ["python", "main.py"]
