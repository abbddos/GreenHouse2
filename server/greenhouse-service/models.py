from database import db 
import datetime 

class Greenhouse(db.Model):
    __tablename__ = 'greenhouse'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    location = db.Column(db.String(100), nullable = False)
    
    
    def __init__(self, name, location):
        self.name = name 
        self.location = location
        
    
    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "location" : self.location  
        }