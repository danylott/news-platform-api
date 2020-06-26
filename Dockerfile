FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /test_task
WORKDIR /test_task
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps
COPY requirements.txt /test_task/
RUN pip install -r requirements.txt
COPY . /test_task/
