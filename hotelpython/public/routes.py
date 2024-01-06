from flask import Blueprint, render_template

public = Blueprint('public', __name__, template_folder="templates")

HOTEL = "The Lee" # load from db

@public.route("/")
def index():
  elements = {"title": "About Us", "navbrand": HOTEL}
  return render_template("index.html", elements=elements)


@public.route("/about")
def about():
  elements = {"title": "About Us", "navbrand": HOTEL}
  return render_template("about.html", elements=elements)


@public.route("/contact")
def contact():
  elements = {"title": "Contact Us", "navbrand": HOTEL}
  return render_template("contact.html", elements=elements)


@public.route("/book-now")
def book_now():
  elements = {"title": "Book Today", "navbrand": HOTEL}
  return render_template("book-now.html", elements=elements)


@public.route("/login")
def login():
  elements = {"title": "Welcome Back", "navbrand": HOTEL}
  return render_template("login.html", elements=elements)

