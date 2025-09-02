from database import db
import datetime 

class FansActuator(db.Model):
    __tablename__ = 'fans-actuator'
    id = db.Column(db.Integer, primary_key = True)
    greenhouse_id = db.Column(db.Integer, nullable = False)
    status = db.Column(db.String, default = "OFF", nullable = False)
    manual_override = db.Column(db.String, default = "Auto", nullable = False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
    
    
    def __init__(self, greenhouse_id, status, manual_override):
        self.greenhouse_id = greenhouse_id
        self.status = status 
        self.manual_override = manual_override
        
        
    def serialize(self):
        return {
            "id": self.id,
            "greenhouse_id": self.greenhouse_id,
            "timestamp": self.timestamp,
            "status": self.status,
            "manual_override": self.manual_override
        } 
        
    