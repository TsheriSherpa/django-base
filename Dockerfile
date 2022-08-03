FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --virtual python3-dev musl-dev gcc build-base \
    && apk add --no-cache mariadb-dev

RUN pip install --upgrade pip

RUN addgroup -S docker && adduser -S docker -G docker

USER docker

WORKDIR /app

COPY requirements.txt .

RUN pip install -r ./requirements.txt

COPY . /app

USER root

RUN chown -R docker:docker /app

USER docker