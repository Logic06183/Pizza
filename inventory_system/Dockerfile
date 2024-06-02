# Use the official Python slim image from the Docker Hub
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Install cron and ensure valid GPG keys
RUN apt-get update && apt-get install -y gnupg2
RUN apt-key adv --fetch-keys http://deb.debian.org/debian-archive/debian-archive-keyring.gpg
RUN apt-get update && apt-get install -y cron

# Collect static files
RUN python manage.py collectstatic --noinput

# Add the cron job
RUN echo "0 0 * * * /usr/local/bin/python /app/manage.py clear_orders" > /etc/cron.d/clear_orders
RUN chmod 0644 /etc/cron.d/clear_orders

# Apply the cron job
RUN crontab /etc/cron.d/clear_orders

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Set the environment variable for the port
ENV PORT 8080

# Expose the port
EXPOSE 8080

# Start the cron service and the Gunicorn server using the PORT environment variable
CMD cron && exec gunicorn --bind :$PORT --workers 1 --threads 8 inventory_system.wsgi:application
