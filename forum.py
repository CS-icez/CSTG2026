from flask import (
    Blueprint, render_template, request, redirect, url_for
)

from CSTG2026.db import get_db

bp = Blueprint('forum', __name__, url_prefix='/forum')

@bp.route('/index')
def index():
    return render_template('forum/index.html')

@bp.route('/section')
def section():
    return render_template('forum/section.html')

@bp.route('/post')
def post():
    return render_template('forum/post.html')

