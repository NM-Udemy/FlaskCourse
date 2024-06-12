from flask import Blueprint

account_bp = Blueprint('account', __name__, url_prefix='/account')

from . import views, models
