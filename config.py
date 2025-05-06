import os

class Config:
    """Application configuration settings"""
    
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-for-glammate')
    DEBUG = os.environ.get('FLASK_DEBUG', True)
    
    # Database settings
    MONGODB_SETTINGS = {
        'host': os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/glammate')
    }
    
    # AWS SES settings
    AWS_REGION = os.environ.get('AWS_REGION', 'us-east-1')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
    
    # Email settings
    SENDER_EMAIL = os.environ.get('SENDER_EMAIL', 'kaniskasritsp@gmail.com')
    RECIPIENT_EMAIL = os.environ.get('RECIPIENT_EMAIL', 'kaniskasritsp@gmail.com')