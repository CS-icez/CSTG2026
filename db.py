import pymysql
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(
            host='localhost',
            user='root',
            password='pku170730',
            port=3306,
            db='cstg'
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# https://www.cnblogs.com/heyouxin/p/14026986.html
def parse_sql_file(filename):
    with current_app.open_resource(filename) as f:
        data = f.read().decode('utf8')
        lines = data.splitlines()
        sql_data = ''
        for line in lines:
            if len(line) == 0:
                continue
            elif line.startswith("--"):
                continue
            else:
                sql_data += line
        sql_list = sql_data.split(';')[:-1]
        sql_list = [x.replace('\n', ' ') if '\n' in x else x for x in sql_list]
    return sql_list

def execute_sql_list(sql_list):
    db = get_db()
    cursor = db.cursor()
    try:
        for sql in sql_list:
            cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    cursor.close()

def execute_sql_file(filename):
    sql_list = parse_sql_file(filename)
    execute_sql_list(sql_list)

def init_db():
    execute_sql_file('sql/schema.sql')
    with current_app.open_resource('sql/trigger.sql') as f:
        sql = f.read().decode('utf8')
        execute_sql_list([sql])
    # execute_sql_file('sql/trigger.sql')
    execute_sql_file('sql/section.sql')

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Database initialized.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)