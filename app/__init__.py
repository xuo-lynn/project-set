import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Gorilla Gang Portfolio", url=os.getenv("URL"))

@app.route('/about')
def about():
    return render_template('about.html', title="About Me", url=os.getenv("URL"))

@app.route('/experience')
def experience():
    return render_template('experience.html', title="Experience", url=os.getenv("URL"))

@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects", url=os.getenv("URL"))

@app.route('/skills')
def skills():
    return render_template('skills.html', title="Skills", url=os.getenv("URL"))

