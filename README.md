# CSTG 2026

## Usage

### Option1: Local

1. Make sure that you have [Flask](https://flask.github.net.cn), [MySQL](https://www.mysql.com) locally. We are running this project under the environment of Flask 2.3.3 and MySQL 8.2.0. We do not guarantee that this project will run normally under other versions.
2. Replace the password in `db.py` and file path in `init_server.sh` and `start_server.sh` with your own.
3. Run `./init_server.sh` in the parent directory of this project to initialize the database.
4. Run `./start_server.sh` in the parent directory of this project to start the server.
