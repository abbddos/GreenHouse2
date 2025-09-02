from flask import Blueprint
from config import Config
from .helper_functions import _proxy_request 

sensor_moisture_bp = Blueprint('sensor_moisture_bp', __name__)

SENSOR_MOISTURE_SERVICE_URL = Config.SENSOR_MOISTURE_SERVICE_URL

    
@sensor_moisture_bp.route('/', defaults = {'path': ''}, methods = ['GET', 'POST', 'PUT', 'DELETE'])
@sensor_moisture_bp.route('/<path:path>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def proxy_greenhouse_service(path):
    return _proxy_request(SENSOR_MOISTURE_SERVICE_URL, path)