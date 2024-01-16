FROM python:3.11

LABEL authors="SzymKam"

WORKDIR src

ENV PYTOHNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

COPY pyproject.toml .

RUN pip install --upgrade pip && pip install poetry && poetry install --no-cache

RUN mkdir -p /staticfiles

COPY src/ /src/
