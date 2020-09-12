from flask_restful import Resource, reqparse
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from flask import jsonify

class TemSentenceTokenizer(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('sentence',
                        type=str,
                        required=True,
                        help="გთხოვთ შეიყვანოთ სწორი წინადადება")

    def get(self):
        data = TemSentenceTokenizer.parser.parse_args()
        sentence = data['sentence']
        try:
            tokenized_words = word_tokenize(sentence)

        except Exception as error:
            return jsonify({'error' : error}), 400

        else:
            return jsonify({'result': tokenized_words}), 200

class FrequencyDistribution(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('text',
                        type=str,
                        required=True,
                        help="გთხოვთ შეიყვანოთ სწორი ტექსტი")

    def get (self):
        data = FrequencyDistribution.parser.parse_args()
        text = data['text']
        clean_text=word_tokenize(text)
        freqdist=FreqDist(clean_text)



        return {'result': freqdist}


