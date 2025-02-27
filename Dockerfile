#Use a minimal and secure base image : Python 3.11
FROM python:3.11-slim 

# Set a working directory inside the container : COPY, RUN, CMD
WORKDIR /app

# Copy only the necessary files
COPY requirements.txt .

# Install dependencies securely
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables 
ENV SECRET_KEY=${SECRET_KEY}

# Copy the rest of the application files
COPY . .

# Set a non-root user for security 
RUN useradd -m appuser
USER appuser

# Expose the application port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]