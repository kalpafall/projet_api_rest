import os 

class Config:
    SECRET = os.environ.get('SECRET_KEY') or 'dev_secret_key'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt_secret_key'
    DEBUG = True
    # Plus tard DATABASE JWT CONFIGS ETC 
    JWT_SECRET_KEY = 'super-secret-key'  # 🔐 à changer en production
