from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db" 

app.config["SECRET_KEY"] = "c4cc65b56cef9900d5557777b2a01e8f" 

database = SQLAlchemy(app)  
bcrypt = Bcrypt(app)      
login_manager = LoginManager(app) 


login_manager.login_view = "homepage"  


@login_manager.user_loader
def load_user(user_id):
    from fakepinterest.models import Usuario
    return Usuario.query.get(int(user_id)) 

from fakepinterest import routes