from flask import Flask
import sqlite3
import os
app.secret_key = os.urandom(24)
app.database='test.db'

app=Flask(__name__)

@app.route('/')

def welcome():

    return render_template('login.html')
        