from flask import Flask
from flask import render_template, request, redirect, url_for

from apps.ocr.ocr_api import Ocr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/ocr/api/', methods=['POST'])
def ocr():
    pass

if __name__ == '__main__':
    app.run()