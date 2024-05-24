from flask import (
    Blueprint, render_template, request, redirect, url_for, flash
)

from CSTG2026.db import get_db
from CSTG2026.auth import signin_required
from random import randint

bp = Blueprint('home', __name__, url_prefix='/home')

@bp.route('/')
@bp.route('/index')
def index():
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
@signin_required
def submit():
    from . import store_file
    if request.method == 'GET':
        return render_template('home/submit.html')
    
    title = request.form['title']
    abstract = request.form['abstract']
    file = request.files['file']
    error = None
    db = get_db()

    authors = []
    for key in request.form:
        if key.startswith('author'):
            authors.append(request.form[key])

    with db.cursor() as cursor:
        if not title:
            error = 'Title is required.'
        elif not abstract:
            error = 'Abstract is required.'
        elif not file:
            error = 'File is required.'
        elif authors == []:
            error = 'Authors are required.'

        if error is not None:
            flash(error, 'error')
            return render_template('home/submit.html')
        
        ids = []
        for author in authors:
            cursor.execute(
                'SELECT usr_id FROM usr WHERE email = %s',
                (author,)
            )
            item = cursor.fetchone()
            if item is None:
                error = 'Author not found: ' + author
                flash(error, 'error')
                return render_template('home/submit.html')
            ids.append(item[0])

        filename = store_file(file)
        try:
            placeholder = ', '.join(['%s'] * len(ids))
            cursor.execute(
                f"SELECT usr_id FROM usr WHERE type = 'R' and email NOT IN ({placeholder})",
                ids
            )
            reviewers = cursor.fetchall()
            assert len(reviewers) > 0
            idx = randint(0, len(reviewers) - 1)

            cursor.execute(
                'INSERT INTO paper (title, abstract, filename, reviewer_id) VALUES (%s, %s, %s, %s)',
                (title, abstract, filename, reviewers[idx][0])
            )
            paper_id = cursor.lastrowid
            for id in ids:
                cursor.execute(
                    'INSERT INTO publishes (usr_id, paper_id) VALUES (%s, %s)',
                    (id, paper_id)
                )
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)

        flash('You have successfully submitted the paper.', 'info')
        return redirect(url_for('home.index'))
    
@bp.route('/personal_homepage')
def personal_homepage():
    return render_template('home/personal_homepage.html')