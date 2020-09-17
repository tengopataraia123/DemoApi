from flask_restful import Resource, reqparse
from nltk.tokenize import word_tokenize
import nltk

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


class PosTagging(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('text and',
                        type=str,
                        required=True,
                        help="გთხოვთ შეიყვანოთ სწორი წინადადება")

    def get(self):
        data = PosTagging.parser.parse_args()
        text = data['text']
        try:
           tokenized_words = word_tokenize(text)
           tags = nltk.pos_tag(tokenized_words)

        except Exception as error:
            return {'error': error}

        else:
            return {'result': tags}, 200

