import os

class Config:
    # Define the port for the API Gateway itself
    API_GATEWAY_PORT = 5000

    # Define the base URLs for your backend microservices
    
    GREENHOUSE_SERVICE_URL = "http://127.0.0.1:5001"
    
    SENSOR_CO2_SERVICE_URL = "http://127.0.0.1:5002"
    SENSOR_LIGHT_SERVICE_URL = "http://127.0.0.1:5003"
    SENSOR_MOISTURE_SERVICE_URL = "http://127.0.0.1:5004"
    SENSOR_TEMPERATURE_SERVICE_URL = "http://127.0.0.1:5005"
    SENSOR_WIND_SERVICE_URL = "http://127.0.0.1:5006"
    
    ACTUATOR_CURTAINS_SERVICE_URL = "http://127.0.0.1:5007"
    ACTUATOR_FANS_SERVICE_URL = "http://127.0.0.1:5008"
    ACTUATOR_HEATERS_SERVICE_URL = "http://127.0.0.1:5009"
    ACTUATOR_LIGHT_SERVICE_URL = "http://127.0.0.1:5010"
    ACTUATOR_SPRINKLERS_SERVICE_URL = "http://127.0.0.1:5011"
    ACTUATOR_VENTS_SERVICE_URL = "http://127.0.0.1:5012"

    # CORS Configuration
    CORS_ORIGINS = ["http://localhost:3000"]

    # Secret key for Flask sessions and JWT signing
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key_for_the_api_gateway'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'super-secret-jwt-key-change-this-in-production'
    
    # Expiry time for email verification tokens (e.g., 24 hours = 86400 seconds)
    EMAIL_VERIFICATION_TOKEN_EXPIRATION = 86400

    # Frontend URLs for email verification redirects
    FRONTEND_VERIFICATION_SUCCESS_URL = "http://localhost:3000/verify-success"
    FRONTEND_VERIFICATION_FAILURE_URL = "http://localhost:3000/verify-failure"