#!/bin/bash
set -e

if [ ! -d "/var/lib/mysql/mysql" ]; then
    echo "Initializing MySQL data directory..."
    mysqld --initialize-insecure --user=mysql
fi

echo "Starting MySQL server..."
mysqld --user=mysql &

echo "Waiting for MySQL to start..."
while ! mysqladmin ping --silent; do
    sleep 1
done

mysqladmin -u root password "cstg2026";

echo "Initializing database and Flask server..."
export FLASK_APP="/CSTG2026"
cp -r /CSTG2026/resources /uploads
rm -f /CSTG2026/uploads
ln -s /uploads /CSTG2026/uploads
python3 -m flask init-db

echo "Starting Flask server..."
python3 -m flask run --host=0.0.0.0

