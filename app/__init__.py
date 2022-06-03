import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Gorilla Gang Portfolio", url=os.getenv("URL"))

@app.route('/xuo')
def index():
    return render_template('xuo.html', title="Set Lynn Portfolio", url=os.getenv("URL"))

@app.route('/chuu')
def index():
    return render_template('chuu.html', title="Kaitlyn Chau Portfolio", url=os.getenv("URL"))

@app.route('/diaz')
def index():
    return render_template('diaz.html', title="Daniel Diaz Portfolio", url=os.getenv("URL"))





