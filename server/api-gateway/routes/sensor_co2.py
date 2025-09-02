from flask import Blueprint
from config import Config
from .helper_functions import _proxy_request 

sensor_co2_bp = Blueprint('sensor_co2_bp', __name__)

SENSOR_CO2_SERVICE_URL = Config.SENSOR_CO2_SERVICE_URL

    
@sensor_co2_bp.route('/', defaults = {'path': ''}, methods = ['GET', 'POST', 'PUT', 'DELETE'])
@sensor_co2_bp.route('/<path:path>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def proxy_greenhouse_service(path):
    return _proxy_request(SENSOR_CO2_SERVICE_URL, path)