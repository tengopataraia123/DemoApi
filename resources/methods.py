from flask_restful import Resource, reqparse
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.probability import FreqDist
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
            return {'error' : error}

        else:
            return {'result': tokenized_words}, 200

class SentTokenizer(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('teqsti',
                        type=str,
                        required=True,
                        help="გთხოვთ შეიყვანოთ სწორი ტექსტი")

    def get (self):
        data = SentTokenizer.parser.parse_args()
        teqsti = data['teqsti']
        clean_text=sent_tokenize(teqsti)
        freqdist=FreqDist(clean_text)



        return {'result': freqdist}


