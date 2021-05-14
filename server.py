import flask
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


@app.route('/')
def get_qr():
    img_buf = BytesIO()
    img = generate_qr('www.python.org')
    img.save(img_buf)
    img_buf.seek(0)
    return flask.send_file(img_buf, mimetype='image/png')

if __name__=='__main__':
    app.run(debug=True)