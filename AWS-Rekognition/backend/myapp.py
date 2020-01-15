from flask import Flask

app = Flask(__name__)

@app.route("/get_picture/", methods=['GET', 'POST'])
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    # run the app locally on the given port
    app.run(host='0.0.0.0', port=5000)