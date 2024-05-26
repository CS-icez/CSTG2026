from flask import (
    Blueprint, render_template, g, redirect, url_for, flash, request
)

from CSTG2026.db import get_db

bp = Blueprint('forum', __name__, url_prefix='/forum')

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('forum/index.html')

@bp.route('/section/<sec_name>', methods=('GET', 'POST'))
def section(sec_name):
    db = get_db()
    sec_list = ['General', 'AI', 'Networks', 'Architecture', 'Cryptography']
    if sec_name not in sec_list:
        flash('Section not found')
        return redirect(url_for('forum.index'))
    
    sec_id = 0
    with db.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM section WHERE title = %s', (sec_name,)
        )
        sec_id = cursor.fetchone()[0]
    
    if request.method == 'GET':
        with db.cursor() as cursor:
            cursor.execute(
                'SELECT * FROM post WHERE sec_id = %s', (sec_id,)
            )
            posts = cursor.fetchall()
            
            def get_name(usr_id):
                cursor.execute(
                    'SELECT name FROM usr WHERE usr_id = %s', (usr_id,)
                )
                return cursor.fetchone()[0]
            
            posts = [(post[0], post[1], post[2], post[3], get_name(post[4]),
                post[5], post[6]) for post in posts]

        return render_template('forum/section.html', sec_name=sec_name, posts=posts)
    
    print(request.form)
    title = request.form['title']
    content = request.form['content']
    pub_id = g.usr[0]
    error = None

    if not title:
        error = 'Title is required.'
    elif not content:
        error = 'Content is required.'

    if error is not None:
        flash(error, 'error')
        return redirect(url_for('forum.section', sec_name=sec_name))
    
    with db.cursor() as cursor:
        cursor.execute(
            'INSERT INTO post (title, content, sec_id, pub_id) VALUES (%s, %s, %s, %s)',
            (title, content, sec_id, pub_id)
        )
        db.commit()
        flash('Post published.', 'info')
        return redirect(url_for('forum.section', sec_name=sec_name))


@bp.route('/post')
def post():
    return render_template('forum/post.html')

@bp.before_request
def signin_required():
    if g.usr is None:
        flash('Please sign in first.', 'error')
        return redirect(url_for('home.index'))
    