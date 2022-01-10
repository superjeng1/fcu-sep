from flask import (
   Blueprint, flash, g, redirect, render_template, request, url_for
)

from courseSelect.auth import login_required
from courseSelect.db import get_db

bp = Blueprint('search', __name__, url_prefix='/search')


@bp.route('/', methods=('GET', 'POST'))
@login_required
def index():
    courses = []
    if request.method == 'POST':
        name = request.form['name']
        error = None

        if not name:
            error = '請輸入課程名稱'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            courses = db.execute(
                'SELECT * FROM course WHERE name LIKE ? LIMIT 100',
                ['%'+name+'%']
            )

    return render_template('search/index.html', courses=courses)
