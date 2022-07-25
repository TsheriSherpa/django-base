FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add python3-dev musl-dev gcc build-base  \
    && apk add --no-cache mariadb-dev

RUN pip install --upgrade pip

WORKDIR /app
COPY requirements.txt .
RUN pip install -r /requirements.txt
COPY . /app


