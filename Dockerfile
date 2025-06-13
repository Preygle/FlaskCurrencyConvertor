# Use Python 3.11 slim image as base (light weight and efficient)
FROM python:3.11-slim

# Set working directory as app in container
WORKDIR /app

# Copy requirements file first as it is less likely to change then lets say backend code
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Running on port 5000
EXPOSE 5000

# Setting up environment variables
ENV FLASK_APP=main.py
ENV FLASK_ENV=production

# Run the application (equivalent to python main.py)
CMD ["python", "main.py"]