FROM python:3.11-slim

# Install system deps + Node.js
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Python deps
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Install Tailwind dependencies
RUN python manage.py tailwind install

# Expose port
EXPOSE 8000

# Run both Django + Tailwind
CMD sh -c "python manage.py tailwind start & python manage.py runserver 0.0.0.0:8000"
