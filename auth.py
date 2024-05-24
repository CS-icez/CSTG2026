# https://flask.github.net.cn/tutorial/views.html

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from CSTG2026.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup', methods=('GET', 'POST'))
def signup():
    if request.method == 'GET':
        return render_template('auth/signup.html')

    name = request.form['name']
    gender = request.form['gender']
    email = request.form['email']
    passwd = request.form['passwd']
    profile = request.form['profile']
    type = request.form['role']
    db = get_db()
    error = None

    with db.cursor() as cursor:
        if not name:
            error = 'usrname is required.'
        elif not gender:
            error = 'Gender is required.'
        elif not email:
            error = 'Email is required.'
        elif not passwd:
            error = 'Password is required.'
        elif not profile:
            error = 'Profile is required.'
        elif not type:
            error = 'Type is required.'

        if error is None:
            cursor.execute('SELECT usr_id FROM usr WHERE email = %s', (email,))
            if cursor.fetchone() is not None:
                error = 'This email is already registered.'

        if error is not None:
            flash(error, 'error')
            return render_template('auth/signup.html')
        
        print(generate_password_hash(passwd))

        cursor.execute(
            'INSERT INTO usr (name, gender, email, passwd, profile, type) VALUES (%s, %s, %s, %s, %s, %s)',
            (name, gender, email, generate_password_hash(passwd), profile, type)
        )
        db.commit()
        flash('You have successfully signed up.', 'info')
        return redirect(url_for('home.index'))


@bp.route('/signin', methods=('POST',))
def signin():
    email = request.form['email']
    passwd = request.form['passwd']
    db = get_db()
    error = None

    with db.cursor() as cursor:
        if not email:
            error = 'Email is required.'
        elif not passwd:
            error = 'Password is required.'

        if error is None:
            cursor.execute(
                'SELECT * FROM usr WHERE email = %s', (email,)
            )
            if (usr := cursor.fetchone()) is None:
                error = 'This email is not registered.'
            elif not check_password_hash(usr[4], passwd):
                error = 'Incorrect password.'

        if error is not None:
            flash(error, 'error')
            return redirect(url_for('home.index'))

        session.clear()
        session['usr_id'] = usr[0]
        flash('You have successfully signed in.', 'info')
        return redirect(url_for('home.index'))

@bp.before_app_request
def load_logged_in_user():
    usr_id = session.get('usr_id')

    if usr_id is None:
        g.usr = None
    else:
        with get_db().cursor() as cursor:
            cursor.execute(
                'SELECT * FROM usr WHERE usr_id = %s', (usr_id,)
            )
            g.usr = cursor.fetchone()

@bp.route('/signout')
def signout():
    session.clear()
    return redirect(url_for('home.index'))

def signin_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.usr is None:
            flash('Sign in required.', 'error')
            return redirect(url_for('home.index'))
        return view(**kwargs)
    return wrapped_view
