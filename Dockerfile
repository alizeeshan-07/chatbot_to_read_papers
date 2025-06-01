# Use official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Set environment variable for Anthropic API key (passed at runtime)
ENV ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}

# Default command to run your chatbot
CMD ["python", "chatbot.py"]
