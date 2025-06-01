import os

postgre_local_base = "postgresql://postgres:username@localhost/salons"
    
class TestingConfig():
        
        TESTING = True
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
        SQLALCHEMY_DATABASE_URI = "postgresql://salonapi_user:UDCYfmsCp7DYWk2ar4ssjzYGfGmjJf31@dpg-d0tvqoadbo4c73a7qpog-a.oregon-postgres.render.com/salonapi"

        
class DevelopmentConfig():
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
        SQLALCHEMY_DATABASE_URI = "postgresql://salonapi_user:UDCYfmsCp7DYWk2ar4ssjzYGfGmjJf31@dpg-d0tvqoadbo4c73a7qpog-a/salonapi"
        DEBUG = True
        DEVELOPMENT = True
        
class ProductionConfig():
        
        SECRET_KEY = 'my_precious'
        DEBUG = True
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")

# postgresql://salonapi_user:UDCYfmsCp7DYWk2ar4ssjzYGfGmjJf31@dpg-d0tvqoadbo4c73a7qpog-a/salonapi