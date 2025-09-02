from flask import Blueprint
from config import Config
from .helper_functions import _proxy_request 

greenhouse_bp = Blueprint('greenhouse_bp', __name__)

GREENHOUSE_SERVICE_URL = Config.GREENHOUSE_SERVICE_URL

    
@greenhouse_bp.route('/', defaults = {'path': ''}, methods = ['GET', 'POST', 'PUT', 'DELETE'])
@greenhouse_bp.route('/<path:path>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def proxy_greenhouse_service(path):
    return _proxy_request(GREENHOUSE_SERVICE_URL, path)