from flask import Flask, jsonify
from flask_cors import CORS
from config import Config # Import our configuration

app = Flask(__name__)

app.config.from_object(Config)

CORS(app, resources={r"/*": {"origins": Config.CORS_ORIGINS}})

# --- Blueprint Imports ---
from routes.greenhouse import greenhouse_bp

from routes.sensor_co2 import sensor_co2_bp
from routes.sensor_light import sensor_light_bp
from routes.sensor_moisture import sensor_moisture_bp 
from routes.sensor_temperature import sensor_temperature_bp
from routes.sensor_wind import sensor_wind_bp

from routes.actuator_curtains import actuator_curtains_bp
from routes.actuator_fans import actuator_fans_bp
from routes.actuator_heaters import actuator_heaters_bp
from routes.actuator_light import actuator_light_bp
from routes.actuator_sprinklers import actuator_sprinklers_bp
from routes.actuator_vents import actuator_vents_bp

# --- Blueprint Registrations ---
app.register_blueprint(greenhouse_bp, url_prefix = "/api/v1/greenhouse")

app.register_blueprint(sensor_co2_bp, url_prefix = "/api/v1/co2_sensor")
app.register_blueprint(sensor_light_bp, url_prefix = "/api/v1/light_sensor")
app.register_blueprint(sensor_moisture_bp, url_prefix = "/api/v1/moisture_sensor")
app.register_blueprint(sensor_temperature_bp, url_prefix = "/api/v1/temperature_sensor")
app.register_blueprint(sensor_wind_bp, url_prefix = "/api/v1/wind_sensor")

app.register_blueprint(actuator_curtains_bp, url_prefix = "/api/v1/curtains_actuator")
app.register_blueprint(actuator_fans_bp, url_prefix = "/api/v1/fans_actuator")
app.register_blueprint(actuator_heaters_bp, url_prefix = "/api/v1/heaters_actuator")
app.register_blueprint(actuator_light_bp, url_prefix = "/api/v1/light_actuator")
app.register_blueprint(actuator_sprinklers_bp, url_prefix = "/api/v1/sprinklers_actuator")
app.register_blueprint(actuator_vents_bp, url_prefix = "/api/v1/vents_actuator")


@app.route('/')
def home():
    """Root endpoint for the API Gateway."""
    return jsonify({"message": "API Gateway is running!", "status": "OK", "version": "1.0"})

if __name__ == '__main__':
    # The API Gateway typically runs on a standard port like 5000
    app.run(port=Config.API_GATEWAY_PORT, debug=True)