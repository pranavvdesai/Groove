from flask import Flask
import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.secret_key=os.urandom(24)

conn=mysql.connector.connect(host="remotemysql.com",user=os.getenv("DB_USER"),password=os.getenv("DB_PASS"),database=os.getenv("DB_NAME"))
cursor=conn.cursor()

from app import api
from app.users.auth_routes import users
from app.main.routes import main
from app.maps.map_routes import maps

app.register_blueprint(users)
app.register_blueprint(main)
app.register_blueprint(maps)

from app import matching
from app import ml

