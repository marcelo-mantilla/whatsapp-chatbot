from flask import Flask
from whatsapp.router import whatsapp


app = Flask(__name__)
app.register_blueprint(whatsapp)

@app.route('/')
def hello_world():
    return 'Hello, World!'


app.run(port=5000)
