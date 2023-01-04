from flask import Blueprint

sample = Blueprint('sample', __name__)


@sample.route('/', methods=['GET'])
def index():
    return 'hello'
