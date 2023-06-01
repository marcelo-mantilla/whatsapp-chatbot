from flask import request, Blueprint


status_router = Blueprint('status', __name__)

@status_router.route('/', methods=['GET'])
def get_status():
    return 'OK'
