import flask
from flask.globals import request
import qrcode
from io import BytesIO
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

def generate_qr(data):
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10,
                       border=4)

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    return img


@app.route('/', methods=['GET', 'POST'])
def get_qr():
    data = None

    if request.method=="GET":
        data = "Hello World!"
    else :
        data = request.json['data']
    if not data:
        data = "No data given!"
    img_buf = BytesIO()
    img = generate_qr(data)
    img.save(img_buf)
    img_buf.seek(0)
    return flask.send_file(img_buf, mimetype='image/png')

if __name__=='__main__':
    app.run(debug=True)