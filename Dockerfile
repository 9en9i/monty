# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster as builder

ENV APP_HOME=/usr/src/monty \
    TZ=UTC

ENV PYTHONPATH=$APP_HOME

WORKDIR $APP_HOME

RUN apt-get update && pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY . .