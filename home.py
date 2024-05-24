from flask import (
    Blueprint, render_template, request, redirect, url_for, g
)

from CSTG2026.db import get_db

bp = Blueprint('home', __name__, url_prefix='/home')

@bp.route('/')
@bp.route('/index')
def index():
    print(g.usr)
    return render_template('home/index.html')

@bp.route('/call_for_papers')
def call_for_papers():
    return render_template('home/call_for_papers.html')

@bp.route('/conference_policies')
def conference_policies():
    return render_template('home/conference_policies.html')

@bp.route('/cstg_conferences')
def cstg_conferences():
    return render_template('home/cstg_conferences.html')

@bp.route('/submit', methods=('GET', 'POST'))
def submit():
    from . import store_file
    if request.method == 'GET':
        return render_template('home/submit.html')
    
    title = request.form['title']
    abstract = request.form['abstract']
    file = request.files['file']
    error = None
    db = get_db()

    with db.cursor() as cursor:
        if not title:
            error = 'Title is required.'
        elif not abstract:
            error = 'Abstract is required.'
        elif not file:
            error = 'File is required.'

        if error is not None:
            flash(error)
            return render_template('home/submit.html')

        filename = store_file(file)
        cursor.execute(
            'INSERT INTO paper (title, abstract, filename) VALUES (%s, %s, %s)',
            (title, abstract, filename)
        )
        db.commit()
        return redirect(url_for('home.index'))
    
@bp.route('/personal_homepage')
def personal_homepage():
    return render_template('home/personal_homepage.html')