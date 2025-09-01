from flask import Flask, jsonify, request
from flask_cors import CORS 
from models import Greenhouse 
from database import db, init_db 
from config import Config 

app  = Flask(__name__)

app.config.from_object(Config)
init_db(app)

CORS(app, resources={r"/*": {"origins": Config.CORS_ORIGINS}})

app.route('/', methods = ['POST'])
def create_greenhouse():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error":"No data provided"}), 400
        
        new_greenhosue = Greenhouse(
            name = data.get('name'),
            location = data.get('location')
        )
        
        db.session.add(new_greenhosue)
        db.session.commit()
        return jsonify(new_greenhosue.serialize()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}), 500
    
    

app.route('/', methods = ['GET'])
def get_all_greenhouses():
    try:
        all_greenhouses = Greenhouse.query.all()
        greenhouse_list = [greenhouse.serialize() for greenhouse in all_greenhouses]
        return jsonify(greenhouse_list), 201
    
    except Exception as e:
        return jsonify({"error":str(e)}), 500
    
    
        
app.route('/<int:greenhouse_id', methods = ['GET'])
def get_greenhouse_by_id(greenhouse_id):
    try:
        greenhouse = Greenhouse.get(greenhouse_id = greenhouse_id)
        if not greenhouse:
            return jsonify({"error":"Greenhouse not found"}), 404
        
        return jsonify(greenhouse.serialize()), 201
    
    except Exception as e:
        return jsonify({"error":str(e)}), 500
    
    
    
app.route('/<int:greenhouse_id', methods = ['PUT'])
def update_greenhouse(greenhouse_id):
    
    data = request.get_json()
    
    try:
        greenhouse = Greenhouse.get(greenhouse_id = greenhouse_id)
        if not greenhouse:
            return jsonify({"error":"Greenhouse not found"}), 404 
        
        greenhouse.name = data.get('name')
        greenhouse.location = data.get('location')
        
        db.session.commit()
        return jsonify(greenhouse.serialize()), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
    
app.route('/<int:greenhouse_id', methods = ['DELETE'])
def delete_greenhouse(greenhouse_id):
    try:
        greenhouse = Greenhouse.get(greenhouse_id = greenhouse_id)
        if not greenhouse:
            return jsonify({"error":"Greenhouse not found"}), 404
        
        db.session.delete(greenhouse)
        db.session.commit()
        return jsonify({"message": "Greenhouse deleted successfully"}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500       


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
    app.run(port = 5001, debug = True)