FROM python:3.12.4-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./pyproject.toml .
RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY . .