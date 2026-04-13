from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)



class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

    def __init__(self, book_name, author, publisher):
        self.book_name = book_name
        self.author = author
        self.publisher = publisher



class BookSchema(ma.Schema):
    class Meta:
        fields = ("id", "book_name", "author", "publisher")


book_schema = BookSchema()
books_schema = BookSchema(many=True)



with app.app_context():
    db.create_all()



@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Book CRUD API is running"})



@app.route("/book", methods=["POST"])
def add_book():
    book_name = request.json["book_name"]
    author = request.json["author"]
    publisher = request.json["publisher"]

    new_book = Book(book_name, author, publisher)
    db.session.add(new_book)
    db.session.commit()

    return book_schema.jsonify(new_book)



@app.route("/books", methods=["GET"])
def get_books():
    all_books = Book.query.all()
    result = books_schema.dump(all_books)
    return jsonify(result)


@app.route("/book/<id>", methods=["GET"])
def get_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({"message": "Book not found"}), 404
    return book_schema.jsonify(book)



@app.route("/book/<id>", methods=["PUT"])
def update_book(id):
    book = Book.query.get(id)

    if not book:
        return jsonify({"message": "Book not found"}), 404

    book.book_name = request.json["book_name"]
    book.author = request.json["author"]
    book.publisher = request.json["publisher"]

    db.session.commit()
    return book_schema.jsonify(book)



@app.route("/book/<id>", methods=["DELETE"])
def delete_book(id):
    book = Book.query.get(id)

    if not book:
        return jsonify({"message": "Book not found"}), 404

    db.session.delete(book)
    db.session.commit()

    return book_schema.jsonify(book)


if __name__ == "__main__":
    app.run(debug=True)