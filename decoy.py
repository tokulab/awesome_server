from flask import Flask
from flask import render_template, request, redirect, url_for

from apps.ocr.ocr_api import Ocr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/apis/ocr/direct', methods=['GET', 'POST'])
def ocr_direct():
    # ocr = Ocr('./config.yaml')
    # img = request.data
    print(request.files['file'])
    # b64 = ocr.posted_img(request.data)
    # print(b64)
    return request.files['file'].filename
if __name__ == '__main__':
    app.run(debug=True, port=4999)