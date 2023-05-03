FROM python:3.9
WORKDIR /app
COPY . /app
#RUN useradd -ms /bin/bash rupali
#USER rupali
#RUN python -m venv /home/myuser/venv
#ENV PATH="/home/myuser/venv/bin:$PATH"
RUN pip install --upgrade pip && pip install Django==3.2
#ENV DJANGO_SETTINGS_MODULE=ParkTicketManagement.settings
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
