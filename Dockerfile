FROM python:3.9


WORKDIR /app


COPY . /app

# Create a new user and switch to that user
RUN useradd -ms /bin/bash myuser
USER myuser

# Set up a virtual environment and install the required packages
RUN python -m venv /home/myuser/venv
ENV PATH="/home/myuser/venv/bin:$PATH"
RUN pip install --upgrade pip && pip install Django==3.2

# Set the environment variable for the Django settings module
ENV DJANGO_SETTINGS_MODULE=ParkTicketManagement.settings

# Expose port 8000 for the Django app
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
