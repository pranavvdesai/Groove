from flask import Flask
import os
import mysql.connector

app = Flask(__name__)
app.secret_key=os.urandom(24)

conn=mysql.connector.connect(host="remotemysql.com",user="9YwiYaINDg",password="WB2u9rVHb5",database="9YwiYaINDg")
cursor=conn.cursor()

from app import api
from app import authentication
from app import maps
from app import matching
from app import ml
