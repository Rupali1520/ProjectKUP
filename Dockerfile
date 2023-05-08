FROM python:3.9
WORKDIR /app
COPY . /app

RUN pip install --upgrade pip && pip install Django==3.2

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]


#kjkj
