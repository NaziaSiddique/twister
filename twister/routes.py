"""
imports render_template to use Flask functionality
imports app and db from twister package
"""
from flask import render_template
from twister import app, db
#from twister.models import Category, Task


@app.route("/")
def home():
    """
to get the app running, create a basic app route
using the root-level directory of slash
this will be used to target the function, 'home'
the function 'home' will return the rendered-template
of 'base.html'
    """
    return render_template("base.html")
