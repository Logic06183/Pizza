# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Set the environment variable for the port
ENV PORT 8080

# Expose the port
EXPOSE 8080

# Start the Gunicorn server using the PORT environment variable
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 inventory_system.wsgi:application
