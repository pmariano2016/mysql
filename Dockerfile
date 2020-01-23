FROM python:3.8

RUN apt-get update && \
    apt-get install -y \
        build-essential \
        curl \
        default-libmysqlclient-dev && \
    apt-get clean && \
    rm -r /var/lib/apt/lists/*
RUN pip install --no-cache-dir \
        mysqlclient \
        SQLAlchemy \
        sqlacodegen
