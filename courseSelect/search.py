from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from courseSelect.auth import login_required

bp = Blueprint('search', __name__, url_prefix='/search')


@bp.route('/', methods=('GET', 'POST'))
@login_required
def create():
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
            return redirect(url_for('search.index'))

    return render_template('search/index.html')
