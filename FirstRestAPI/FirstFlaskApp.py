from flask import Flask

app = Flask(__name__)

##The request that flask will process
@app.route('/')
def home():
    return "Hello World!"

app.run(port=5000)