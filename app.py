from flask import Flask, redirect
from flask_restful import Api

from resources.methods import TemSentenceTokenizer, PosTagging

app = Flask(__name__)

api = Api(app)

@app.route('/')
def home():
    return redirect('https://github.com/temurchichua/DemoApi')

api.add_resource(TemSentenceTokenizer, '/TemSenTok')
api.add_resource(PosTagging, '/PosTag')

if __name__ == "__main__":
    app.run(port = 5000, debug = True)
