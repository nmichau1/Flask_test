import flask 
from flask import Flask
from flask import render_template 

app = Flask(__name__)

@app.route('/',methods=["GET"])
def hello():
	return "TEST" #render_template('/index.html')

