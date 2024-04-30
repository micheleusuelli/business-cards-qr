from flask import Flask, render_template, request
import qrcode
from vcardgen import VCardGenerator
import glob


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr_code():
    data = {}
    for key, value in request.form.items():
        data[key] = value
    vcard_generator = VCardGenerator('')
    vcard = vcard_generator.generate_vcard_from_json(data)
    qr_img = vcard_generator.create_qr_code(vcard)
    qr_img.save('static/qr_code.png')  # Save the QR code image
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)


