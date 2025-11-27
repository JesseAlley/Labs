# After watching the video, create a CRUD API for a Book instead of a Drink in the video example above. 
# The Book model should have the following parameters:
# id
# book_name
# author
# publisher

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String(80), unique = True, nullable = false)
    author = db.Column(db.String(25))
    publisher = db.Column(db.String(80))

    def __repr__(self):
        return f"{self.id - self.name - self.author - self.publisher}"


@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    books = Books.query.all()
    output = []
    for book in books:
        drink_data = {'name': book.name, 'author': book.author }
        output.append(book_data)
    return {"books": output}

@app.route('/books/<id>')
def get_drink(id):
    book = Book.query.get_or_404(id)
    return {"name": book.name, "author": book.author}

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(name = request.json['name'], description=request.json['description'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/books/<id>', methods = ['DELETE'])
def delete_book():
    book = Book.query.get(id)
    if book is None:
        return{"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"messeage": "yeet!@"}