from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from courseSelect.auth import login_required
from courseSelect.db import get_db

bp = Blueprint('list', __name__, url_prefix='/list')


@bp.route('/', methods=('GET', 'POST'))
@login_required
def list():
    db = get_db()
    #posts = db.execute(
    #    'SELECT p.id, title, body, created, author_id, username'
    #    ' FROM post p JOIN user u ON p.author_id = u.id'
    #    ' ORDER BY created DESC'
    #).fetchall()
    classes = db.execute(
        'SELECT name, teacher_name FROM course WHERE id IN (SELECT course_id FROM selection WHERE student_id = ?)',
        [g.user['id']]
    ).fetchall()

    return render_template('list/index.html', classes=classes)
