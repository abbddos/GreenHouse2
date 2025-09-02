from flask import Blueprint
from config import Config
from .helper_functions import _proxy_request 

sensor_light_bp = Blueprint('sensor_light_bp', __name__)

SENSOR_LIGHT_SERVICE_URL = Config.SENSOR_LIGHT_SERVICE_URL

    
@sensor_light_bp.route('/', defaults = {'path': ''}, methods = ['GET', 'POST', 'PUT', 'DELETE'])
@sensor_light_bp.route('/<path:path>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def proxy_greenhouse_service(path):
    return _proxy_request(SENSOR_LIGHT_SERVICE_URL, path)