class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///auto_repair_shop.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your_jwt_secret_key'  # Change this to a random secret key
