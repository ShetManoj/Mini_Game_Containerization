# Stage 1
FROM python:3.9 AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file to install dependencies first
COPY requirements.txt .

# Install dependencies in a virtual environment
RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files to the container
COPY . .

# Stage 2: Production Stage
FROM python:3.9-slim

# Set environment variables for Python
ENV PATH="/opt/venv/bin:$PATH"

# Set the working directory
WORKDIR /app

# Copy the virtual environment from the builder stage
COPY --from=builder /opt/venv /opt/venv

# Copy only the necessary app files from the build stage
COPY --from=builder /app /app

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
