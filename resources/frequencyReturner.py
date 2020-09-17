from flask_restful import Resource, reqparse
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist


class FrequencyReturner(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('sentence',
                        type=str,
                        required=True,
                        help="გთხოვთ შეიყვანოთ სწორი ტექსტი")
    def get(self):
        data = FrequencyReturner.parser.parse_args()
        sentence = data['sentence']
        clean_text = sent_tokenize(sentence)
        fdist = FreqDist(clean_text)

        return {'result': fdist}