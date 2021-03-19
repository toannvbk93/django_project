FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /django_project
COPY requirements.txt /django_project/
RUN pip3 install -r requirements.txt
COPY . /django_project/
