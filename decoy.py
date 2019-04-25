from flask import Flask
from flask import render_template, request, redirect, url_for, jsonify
from flask_sockets import Sockets
import gevent

from apps.ocr.ocr_api import Ocr

app = Flask(__name__)
# sockets = Sockets(app=app)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/apis/ocr/direct', methods=['GET', 'POST'])
def ocr_direct():
    query = request.args
    ocr = Ocr('./config.yaml')
    gevent.sleep(1)
    img = request.files['file']
    ocr.posted_img(img)
    gevent.sleep(2)
    result = ocr.img_to_str(lang='eng', tesseract_layout=6)
    json_data = ocr.format_to_json(result=result,
                                   name=img.filename,
                                   ensure_ascii=False if query['asc'] == '0' else True,
                                   indent=2,
                                   del_lf=True)

    return json_data


@app.errorhandler(400):
def not_found(err):
    resp = jsonify(
        {
            u'status_code': 404,
            u'message': u'not found.'
        }
    )
    resp.status_code = 404
    return resp


if __name__ == '__main__':
    # app.run(debug=True, port=4999)
    app.run(debug=True)