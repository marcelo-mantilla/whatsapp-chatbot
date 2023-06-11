from flask import request, Blueprint


status = Blueprint('status', __name__)


@status.route('/', methods=['GET'])
def get_status():
    return 'OK'
