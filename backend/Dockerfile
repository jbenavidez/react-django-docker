FROM python:3.9-alpine3.13

ENV PYTHONUNBUFFERED=1

WORKDIR /django_app

COPY requirements.txt /django_app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . ./django_app


