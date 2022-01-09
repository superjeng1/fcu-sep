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
    #db = get_db()
    # db.execute(
    #    'INSERT INTO post (title, body, author_id)'
    #    ' VALUES (?, ?, ?)',
    #    (title, body, g.user['id'])
    # )
    # db.commit()

    return render_template('list/index.html')