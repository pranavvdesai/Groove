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
from app import authentication
from app import maps
from app import matching
from app import ml
