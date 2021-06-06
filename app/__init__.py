from flask import Flask
import os

app = Flask(__name__)
app.secret_key=os.urandom(24)


from app import api
from app import authentication
from app import maps
from app import matching
from app import ml
