from application import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.lname}', '{self.email}')"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(10))
    author = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"