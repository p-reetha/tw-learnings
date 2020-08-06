from flask import Flask, jsonify, request
from sqlalchemy import create_engine

app = Flask(__name__)
app.config['DEBUG'] = True


def connect_db():
    db_connection_string = 'postgresql://postgres:489bb@localhost/bookworld'
    return create_engine(db_connection_string)


@app.route("/")
def index():
    return "Home page of book world!"


@app.route("/all-books", methods=['GET'])
def get_all_books():
    books_from_db = db.execute('select name from public.books;')
    formatted_result = [dict(row) for row in books_from_db]
    return jsonify(formatted_result)


@app.route("/add-book", methods=['POST'])
def add_book():
    arg = request.args['arg']
    db.execute('insert into public.books (name) values ({});'.format(arg))
    return 'Book is added to db'


db = connect_db()
app.run()
