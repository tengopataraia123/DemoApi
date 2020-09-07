from flask_restful import Resource, reqparse
from nltk.tokenize import word_tokenize

class TemSentenceTokenizer(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('sentence',
                        type=str,
                        required=True,
                        help="გთხოვთ შეიყვანოთ სწორი წინადადება")

    def get(self):
        try:
            data = TemSentenceTokenizer.parser.parse_args()
            sentence = data['sentence']

            tokenized_words = word_tokenize(sentence)

        except Exception as error:
            return {'error' : error}

        else:
            return {'result': tokenized_words}, 200

