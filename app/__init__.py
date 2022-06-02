import os
from ssl import HAS_TLSv1_1
from turtle import title
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html',title="My Portfolio", url=os.getenv("URL"))

@app.route('/about')
def about():
    return "<h1>About<h1>"

@app.route('/experience')
def experience():
    return "<h1>Experience<h1>"

@app.route('/projects')
def projects():
    return "<h1>Projects<h1>"

@app.route('/skills')
def skills():
    return "<h1>Skills<h1>"

@app.route('/visited')
def visited():
    return "<h1>Visited<h1>"