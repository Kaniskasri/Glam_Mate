from flask_mongoengine import MongoEngine
from datetime import datetime

# Initialize MongoEngine
db = MongoEngine()

class Appointment(db.Document):
    """Model for beauty parlor appointments"""
    name = db.StringField(required=True)
    location = db.StringField(required=True)
    service = db.StringField(required=True)
    preferred_time = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.utcnow)
    
    meta = {
        'collection': 'appointments',
        'ordering': ['-created_at']
    }
    
    def __str__(self):
        return f"{self.name} - {self.service} at {self.preferred_time}"

class Product(db.Document):
    """Model for beauty products (for the shopping page)"""
    name = db.StringField(required=True)
    description = db.StringField(required=True)
    price = db.FloatField(required=True)
    image_url = db.StringField()
    category = db.StringField()
    in_stock = db.BooleanField(default=True)
    
    meta = {
        'collection': 'products',
        'ordering': ['name']
    }
    
    def __str__(self):
        return f"{self.name} (${self.price})"