from flask import (
    Blueprint, render_template, g, redirect, url_for
)

# from CSTG2026.db import get_db

bp = Blueprint('forum', __name__, url_prefix='/forum')

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('forum/index.html')

@bp.route('/section')
def section():
    return render_template('forum/section.html')

@bp.route('/post')
def post():
    return render_template('forum/post.html')

@bp.before_request
def signin_required():
    if g.usr is None:
        return redirect(url_for('home.index'))
    