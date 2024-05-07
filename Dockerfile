# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Update pip
RUN python -m pip install --upgrade pip

# Install virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy the requirements file and install dependencies
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app will run on
EXPOSE 5050

# CMD ["python", "main.py"]
# Set the command to run the Flask app
CMD ["gunicorn","--config", "gunicorn_config.py", "main:app"]
