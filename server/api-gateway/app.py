from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import requests # For making HTTP requests to other microservices
from flask_jwt_extended import JWTManage
import json 
from config import Config # Import our configuration

app = Flask(__name__)

app.config.from_object(Config)

CORS(app, resources={r"/*": {"origins": Config.CORS_ORIGINS}})

# --- Blueprint Imports ---
from routes.greenhouse import greenhouse_bp 


# --- Blueprint Registrations ---
app.register_blueprint(greenhouse_bp, url_prefix = "/api/v1/greenhouse")


@app.route('/')
def home():
    """Root endpoint for the API Gateway."""
    return jsonify({"message": "API Gateway is running!", "status": "OK", "version": "1.0"})

if __name__ == '__main__':
    # The API Gateway typically runs on a standard port like 5000
    app.run(port=Config.API_GATEWAY_PORT, debug=True)