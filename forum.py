from flask import (
    Blueprint, render_template, g, redirect, url_for, flash, request
)

from CSTG2026.db import get_db

bp = Blueprint('forum', __name__, url_prefix='/forum')
sec_list = ['General', 'AI', 'Networks', 'Architecture', 'Cryptography']

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('forum/index.html')

@bp.route('/section/<sec_name>', methods=('GET', 'POST'))
def section(sec_name):
    db = get_db()
    if sec_name not in sec_list:
        flash('Section not found', 'error')
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
            
            posts = [(p[0], p[1], p[2], p[3], get_name(p[4]), p[5], p[6]) for p in posts]

        return render_template('forum/section.html', sec_name=sec_name, posts=posts)
    
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

@bp.route('/section/<sec_name>/post/<post_id>', methods=('GET', 'POST'))
def post(sec_name, post_id):
    db = get_db()
    if sec_name not in sec_list:
        flash('Section not found', 'error')
        return redirect(url_for('forum.index'))
    
    sec_id = 0
    post = None
    with db.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM section WHERE title = %s', (sec_name,)
        )
        sec_id = cursor.fetchone()[0]
        cursor.execute(
            'SELECT * FROM post WHERE post_id = %s', (post_id,)
        )
        post = cursor.fetchone()
        if post[3] is None or post[3] != sec_id:
            flash('Post not found', 'error')
            return redirect(url_for('forum.section', sec_name=sec_name))
        
    if request.method == 'GET':
        with db.cursor() as cursor:
            cursor.execute(
                'SELECT * FROM reply WHERE post_id = %s', (post_id,)
            )
            replies = cursor.fetchall()
            
            def get_name(usr_id):
                cursor.execute(
                    'SELECT name FROM usr WHERE usr_id = %s', (usr_id,)
                )
                return cursor.fetchone()[0]
            
            replies = [(r[0], r[1], r[2], get_name(r[3]), r[4]) for r in replies]

        return render_template('forum/post.html',
            sec_name=sec_name, post=post, replies=replies)
    
    content = request.form['content']
    pub_id = g.usr[0]

    if not content:
        flash('Content is required.', 'error')
        return redirect(url_for('forum.post', sec_name=sec_name, post_id=post_id))
        
    with db.cursor() as cursor:
        cursor.execute(
            'INSERT INTO reply (content, post_id, pub_id) VALUES (%s, %s, %s)',
            (content, post_id, pub_id)
        )
        db.commit()
        flash('Reply published.', 'info')
        return redirect(url_for('forum.post', sec_name=sec_name, post_id=post_id))    


@bp.before_request
def signin_required():
    if g.usr is None:
        flash('Please sign in first.', 'error')
        return redirect(url_for('home.index'))
    