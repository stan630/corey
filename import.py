import csv
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application.models import Book

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] ='postgresql://postgres:admin@localhost/goodreads'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db = SQLAlchemy(app)


def main():
    f = open("books.csv")
    reader = csv.reader(f)
    for isbn,  title, author, year in reader:
        book = Book(isbn=isbn,  title=title, author=author, year=year)
        db.session.add(book)
        
    db.session.commit()

    
if __name__=="__main__":
    main()