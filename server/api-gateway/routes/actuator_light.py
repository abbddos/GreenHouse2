from flask import Blueprint
from config import Config
from .helper_functions import _proxy_request 

actuator_light_bp = Blueprint('actuator_light_bp', __name__)

ACTUATOR_LIGHT_SERVICE_URL = Config.ACTUATOR_LIGHT_SERVICE_URL

    
@actuator_light_bp.route('/', defaults = {'path': ''}, methods = ['GET', 'POST', 'PUT', 'DELETE'])
@actuator_light_bp.route('/<path:path>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def proxy_greenhouse_service(path):
    return _proxy_request(ACTUATOR_LIGHT_SERVICE_URL, path)