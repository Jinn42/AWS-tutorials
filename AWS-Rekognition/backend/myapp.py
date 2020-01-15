from flask import Flask, request
from flask_cors import CORS
from urllib.request import urlopen
from binascii import a2b_base64

app = Flask(__name__)
CORS(app) #added by me

@app.route("/get_picture/", methods=['GET', 'POST'])
def getpicture():
    imgData = request.get_data()

    data = 'MY BASE64-ENCODED STRING'
    binary_data = a2b_base64(imgData[16:])
    with open('image.jpg', 'wb') as fd:
        fd.write(imgData)

    return "Hello, World!"

if __name__ == "__main__":
    # run the app locally on the given port
    app.run(host='0.0.0.0', port=5000)