FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --virtual .build-deps python3-dev musl-dev gcc  build-base \
    && apk add --no-cache mariadb-dev

RUN pip install --upgrade pip

RUN adduser -D docker

USER docker

WORKDIR /app

COPY requirements.txt /app

RUN pip install --user -r requirements.txt

COPY . /app
