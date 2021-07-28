from flask import Blueprint
from flask_app.models import db, User

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return 'Welcom to Index Page'

@bp.route('/create')
def create():
    return 'Welcom to Create Page'

@bp.route('/update')
def update():
    return 'Welcom to Update Page'