FROM python:3.9-slim

WORKDIR /CSTG2026

COPY . .

RUN apt-get update \
    && apt-get install -y default-mysql-server \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /var/run/mysqld /var/lib/mysql && \
    chown -R mysql:mysql /var/lib/mysql /var/run/mysqld

RUN pip install --no-cache-dir -r requirements.txt

RUN sed -i \
    's/from werkzeug import secure_filename, FileStorage/from werkzeug.utils import secure_filename\nfrom werkzeug.datastructures import FileStorage/' \
    /usr/local/lib/python3.9/site-packages/flask_uploads.py

EXPOSE 5000

ENTRYPOINT ["/CSTG2026/docker-entrypoint.sh"]
