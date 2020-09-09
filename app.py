from flask import Flask, redirect
from flask_restful import Api

from resources.methods import TemSentenceTokenizer
from resources.methods import FrequencyDistribution
from resources.methods import SentenceTokenizer

app = Flask(__name__)

api = Api(app)

@app.route('/')
def home():
    return redirect('https://github.com/temurchichua/DemoApi')

api.add_resource(TemSentenceTokenizer, '/TemSenTok')
api.add_resource(FrequencyDistribution, '/FreqDist')
api.add_resource(SentenceTokenizer ,'/sentence')


if __name__ == "__main__":
    app.run(port = 5000, debug = True)
