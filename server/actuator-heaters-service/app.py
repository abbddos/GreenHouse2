from flask import Flask, jsonify, request
from flask_cors import CORS 
from models import HeatersActuator 
from database import db, init_db 
from config import Config 
 

app  = Flask(__name__)

app.config.from_object(Config)
init_db(app)


app.route('/<int:greenhouse_id>', methods = ['POST'])
def add_status(greenhouse_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error":"No data provided"}), 400
        
        new_status = HeatersActuator(
            greenhouse_id = greenhouse_id,
            status = data.get('status'),
            manual_override = data.get('manual_override')
        )
        
        db.session.add(new_status)
        db.session.commit()
        return jsonify(new_status.serialize()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}), 500
    
    

app.route('/<int_greenhouse_id>/all', methods = ['GET'])
def get_all_readings(greenhouse_id):
    try:
        all_statuses = HeatersActuator.query.filter(greenhouse_id = greenhouse_id).all()
        statuses_list = [status_.serialize() for status_ in all_statuses]
        return jsonify(statuses_list), 201
    
    except Exception as e:
        return jsonify({"error":str(e)}), 500
    
    
        
app.route('/<int:greenhouse_id/latest', methods = ['GET'])
def get_latest_reading(greenhouse_id):
    try:
        latest_status = HeatersActuator.query.filter(greenhouse_id = greenhouse_id).order_by(HeatersActuator.timestamp.desc()).first()
        if not latest_status:
            return jsonify({"error":"Greenhouse not found"}), 404
        
        return jsonify(latest_status.serialize()), 201
    
    except Exception as e:
        return jsonify({"error":str(e)}), 500
        


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
    app.run(port = 5009, debug = True)