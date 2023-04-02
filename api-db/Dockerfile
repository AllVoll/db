FROM python:3.8

MAINTAINER AV

ADD . /app

WORKDIR /app

# Set environment variable for database host
ENV DB_HOST=db

RUN apt-get update && apt-get install -y build-essential redis-server sqlite3 \
    curl software-properties-common

# install nodejs and wscat websocket client
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -

RUN apt-get install -y nodejs && npm install wscat

# install popular Python packages
RUN pip3 install -r requirements.txt

RUN pip install asyncpg

RUN pip install python-multipart

RUN pip install alembic