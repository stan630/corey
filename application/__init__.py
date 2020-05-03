from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']= 'mysecretkey'

app.config["SQLALCHEMY_DATABASE_URI"] ='postgresql://postgres:admin@localhost/goodreads'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db = SQLAlchemy(app)

from application import routes
