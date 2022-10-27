from sre_constants import SUCCESS
from flask import Flask, render_template, request, flash, session, redirect, jsonify, json
from jinja2 import StrictUndefined
from model import connect_to_db, db
import crud
# import requests
import os

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

#render homepage
@app.route("/")
def homepage():
    """View homepage."""
    
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login_user():
    user_name = request.form.get("user_name")
    user = crud.get_user_by_user_name(user_name)
    if not user:
        user = crud.create_user(user_name)
        db.session.add(user)
        db.session.commit()
        session["user_name"] = user.user_name
    else:

        return redirect("/appointments")


@app.route("/appointments")
def show_slots():
    return render_template("appointments.html")



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)