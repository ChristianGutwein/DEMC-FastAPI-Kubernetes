# Build stage
FROM python:3.10-slim

# set /app as working directory inside the container
WORKDIR /app

# Copy requirements.txt first to install dependencies
COPY requirements.txt .

# --no-cache-dir: This option prevents pip from caching the packages which can save some space
RUN pip install --no-cache-dir -r requirements.txt

# Copy app and .env
COPY app/ ./app/
COPY .env .

# The EXPOSE instruction in a Dockerfile indicates which ports the container listens on at runtime, serving as documentation for users and facilitating port mapping when running the container
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]