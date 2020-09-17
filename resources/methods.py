from flask_restful import Resource, reqparse


from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.probability import FreqDist

from flask import jsonify
import nltk

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
            print(f'error: {error}')
            return jsonify({'error': f"დაფიქსირდა შეცდომა: {error}"}), 400

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

class sentTok(Resource):
    parser1 = reqparse.RequestParser()
    parser1.add_argument('text',
                        type=str,
                        required=True,
                        help="გთხოვთ შეიყვანოთ სწორი ტექსტი")


 
class SentenceTokenizer(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('sentence',
                        type=str,
                        required=True,
                        help="გთხოვთ შეიყვანოთ სწორი წინადადება")

    def get(self):
        data = SentenceTokenizer.parser.parse_args()
        sentence = data['sentence']
        try:


            tokenized_words = sent_tokenize(sentence)

        except Exception as error:
            return {'error' : error}

        else:
            return {'result': tokenized_words}, 200


   def get(self):
        data = sentTok.parser1.parse_args()
        text = data['text']
        return {"result": sent_tokenize(text)}
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

