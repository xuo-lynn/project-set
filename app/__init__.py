import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Gorilla Gang Portfolio", url=os.getenv("URL"))

@app.route('/xuo')
def xuo():
    return render_template('xuo.html', title="Set Lynn Portfolio")

@app.route('/chuu')
def chuu():
    return render_template('chuu.html', title="Kaitlyn Chau Portfolio")

@app.route('/chuu/hobbies')
def chuu_hobbies():
    return render_template('chuu_hobbies.html', title="Kaitlyn Chau's Hobbies'")

@app.route('/chuu/travel')
def chuu_travel():
    return render_template('chuu_travel.html', title="Kaitlyn Chau's Travel'")

@app.route('/chuu/experience')
def chuu_experience():
    return render_template('chuu_experience.html')

@app.route('/diaz')
def diaz():
    return render_template('diaz.html', title="Daniel Diaz Portfolio")





