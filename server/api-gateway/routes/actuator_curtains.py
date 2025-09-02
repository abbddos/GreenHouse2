from flask import Blueprint
from config import Config
from .helper_functions import _proxy_request 

actuator_curtains_bp = Blueprint('actuator_curtains_bp', __name__)

ACTUATOR_CURTAINS_SERVICE_URL = Config.ACTUATOR_CURTAINS_SERVICE_URL

    
@actuator_curtains_bp.route('/', defaults = {'path': ''}, methods = ['GET', 'POST', 'PUT', 'DELETE'])
@actuator_curtains_bp.route('/<path:path>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def proxy_greenhouse_service(path):
    return _proxy_request(ACTUATOR_CURTAINS_SERVICE_URL, path)