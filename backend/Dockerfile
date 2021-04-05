FROM python:3.6-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
RUN mkdir /app/static
WORKDIR /app

COPY requirements.txt /app

RUN apk update --no-cache \
    && apk add build-base python3-dev postgresql-dev postgresql-libs libpq --no-cache --virtual .build-deps \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000
