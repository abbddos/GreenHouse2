from flask import Blueprint
from config import Config
from .helper_functions import _proxy_request 

sensor_temperature_bp = Blueprint('sensor_temperature_bp', __name__)

SENSOR_TEMPERATURE_SERVICE_URL = Config.SENSOR_TEMPERATURE_SERVICE_URL

    
@sensor_temperature_bp.route('/', defaults = {'path': ''}, methods = ['GET', 'POST', 'PUT', 'DELETE'])
@sensor_temperature_bp.route('/<path:path>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def proxy_greenhouse_service(path):
    return _proxy_request(SENSOR_TEMPERATURE_SERVICE_URL, path)