from sre_constants import SUCCESS
from flask import Flask, render_template, request, flash, session, redirect, jsonify, json
from model import connect_to_db, db
import crud
import requests
import os

app = Flask(__name__)










if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)