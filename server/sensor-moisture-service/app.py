from flask import Flask, jsonify, request
from flask_cors import CORS 
from models import MoistureSensorTable 
from database import db, init_db 
from config import Config 
import paho.mqtt.client as mqtt 
import os 
import threading 

app  = Flask(__name__)

app.config.from_object(Config)
init_db(app)

CORS(app, resources={r"/*": {"origins": Config.CORS_ORIGINS}})

mqtt_client = mqtt.Client(client_id="GreenHouseAPP") 

def on_connect(client, userdata, flags, rc):
    """Callback for when the client receives a CONNACK response from the broker."""
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {rc}\n")
        
mqtt_client.on_connect = on_connect
mqtt_client.connect("localhost", 1883, 60)
mqtt_client.loop_start()


def mqtt_messaging(reading_):
    if reading_.reading > reading_.setpoint + reading_.margin:
        mqtt_client.publish(f"greenhouse_app/{reading_.greenhouse_id}/sprinklers", '{"command":"OFF"}', retain = True) 
    elif reading_.reading < reading_.setpoint - reading_.margin:
        mqtt_client.publish(f"greenhouse_app/{reading_.greenhouse_id}/sprinklers", '{"command":"ON"}', retain = True)
        
        

app.route('/<int:greenhouse_id>', methods = ['POST'])
def add_reading(greenhouse_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error":"No data provided"}), 400
        
        new_reading = MoistureSensorTable(
            greenhouse_id = greenhouse_id,
            setpoint = data.get('setpoint'),
            margin = data.get('margin'),
            reading = data.get('reading')
        )
        
        db.session.add(new_reading)
        mqtt_messaging(new_reading)
        db.session.commit()
        return jsonify(new_reading.serialize()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}), 500
    
    

app.route('/<int_greenhouse_id>/all', methods = ['GET'])
def get_all_readings(greenhouse_id):
    try:
        all_readings = MoistureSensorTable.query.filter(greenhouse_id = greenhouse_id).all()
        readings_list = [reading_.serialize() for reading_ in all_readings ]
        return jsonify(readings_list), 201
    
    except Exception as e:
        return jsonify({"error":str(e)}), 500
    
    
        
app.route('/<int:greenhouse_id/latest', methods = ['GET'])
def get_latest_reading(greenhouse_id):
    try:
        latest_reading = MoistureSensorTable.query.filter(greenhouse_id = greenhouse_id).order_by(MoistureSensorTable.timestamp.desc()).first()
        if not latest_reading:
            return jsonify({"error":"Greenhouse not found"}), 404
        
        return jsonify(latest_reading.serialize()), 201
    
    except Exception as e:
        return jsonify({"error":str(e)}), 500
        


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
    app.run(port = 5004, debug = True)