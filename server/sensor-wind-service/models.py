from database import db
import datetime 

class WindSensorTable(db.Model):
    __tablename__ = 'wind_sensor_table'
    id = db.Column(db.Integer, primary_key = True)
    greenhouse_id = db.Column(db.Integer, nullable = False)
    reading = db.Column(db.Float, nullable = True)
    setpoint = db.Column(db.Float, nullable = False)
    margin = db.Column(db.Float, nullable = False) 
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
    
    
    def __init__(self, greenhouse_id, setpoint, margin):
        self.greenhouse_id = greenhouse_id
        self.setpoint = setpoint
        self.margin = margin 
        
        
    def serialize(self):
        return {
            "id": self.id,
            "greenhouse_id": self.greenhouse_id,
            "timestamp": self.timestamp,
            "setpoint": self.setpoint,
            "margin": self.margin,
            "reading": self.reading
        } 
        
    