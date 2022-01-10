from flask import (
   Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from courseSelect.auth import login_required
from courseSelect.db import get_db

bp = Blueprint('remove', __name__, url_prefix='/remove')


@bp.route('/', methods=('GET', 'POST'))
@login_required
def remove():
    if request.method == 'POST':
        name = request.form['name']
        error = None

        if not name:
            error = 'Course name is required.'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            # db.execute(
            #    'INSERT INTO post (title, body, author_id)'
            #    ' VALUES (?, ?, ?)',
            #    (title, body, g.user['id'])
            # )
            # db.commit()
            db = get_db()
            db.execute(
               'DELETE FROM selection WHERE course_id = (SELECT id FROM course WHERE name = ?)',
               [name]
            )
            db.commit()
            return redirect(url_for('list.list'))

    return render_template('remove/index.html')
