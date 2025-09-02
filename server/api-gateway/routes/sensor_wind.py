from flask import Blueprint
from config import Config
from .helper_functions import _proxy_request 

sensor_wind_bp = Blueprint('sensor_wind_bp', __name__)

SENSOR_WIND_SERVICE_URL = Config.SENSOR_WIND_SERVICE_URL

    
@sensor_wind_bp.route('/', defaults = {'path': ''}, methods = ['GET', 'POST', 'PUT', 'DELETE'])
@sensor_wind_bp.route('/<path:path>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def proxy_greenhouse_service(path):
    return _proxy_request(SENSOR_WIND_SERVICE_URL, path)