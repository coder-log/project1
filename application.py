import os

from flask import Flask, session, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Debug mode delete on production
app.config['DEBUG'] = True


# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


# Routes ###################################

#Home
@app.route("/")
def index():
    return render_template("index.html")

#Search a book for logged users only

@app.route("/books")
def books():
    return render_template("books.html")

#Single book page with reviews and ratings a info
#TODO - Añadir /books/id o isbn para tomar los datos del libro concreto a mostrar

@app.route("/book")
def book():
    return render_template("book.html")



