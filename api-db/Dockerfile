FROM python:3.8

MAINTAINER AV

ADD . /app

WORKDIR /app

# Set environment variable for database host
ENV DB_HOST=timescale

RUN apt-get update && apt-get install -y build-essential redis-server sqlite3 \
    curl software-properties-common libpq-dev

# install nodejs and wscat websocket client
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -

RUN apt-get install -y nodejs && npm install wscat

RUN python -m pip install --upgrade pip

# install popular Python packages
RUN pip3 install -r requirements.txt

RUN pip install asyncpg

RUN pip install psycopg2-binary

RUN pip install python-multipart

RUN pip install alembic

# Initialize alembic migrations
RUN alembic init migrations

# Copy alembic configuration file to container
COPY alembic.ini .

# Run alembic migrations
#RUN alembic upgrade head

RUN pip install uvicorn

# Start the application
CMD ["uvicorn", "web.main:app", "--host", "0.0.0.0", "--port", "80", "--workers", "4", "--access-log"] 
CMD alembic upgrade head && python /app/app.py