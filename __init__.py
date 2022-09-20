from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY']= os.environ.get("SECRET_KEY")
    
    
    from .post import post as post_blueprint
    app.register_blueprint(post_blueprint)
    from .user import user as user_blutprint
    app.register_blueprint(user_blutprint)
    
    return app
    