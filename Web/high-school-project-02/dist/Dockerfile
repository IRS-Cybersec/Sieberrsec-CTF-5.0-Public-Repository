# Base image
FROM python:3.11-slim as base

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install
# Copy the Python scripts
COPY . .

# Run script 1
CMD ["gunicorn", "-w", "5", "-b", "0.0.0.0:5000", "app:app"]

EXPOSE 5000