from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_cors import CORS


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://emna:134200@localhost/flask'
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
db=SQLAlchemy(app)
CORS(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
from MobileAPP import routes



