from flask_restful import Resource, reqparse
from nltk.tokenize import word_tokenize
import re

class GroupingMultiplePatters(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('sentence',
                        type = str,
                        required = True,
                        help = "გთხოვთ შეიყვანოთ სწორი წინადადება")
    
    def get(self):
        data = GroupingMultiplePatters.parser.parse_args()
        text = data['sentence']
        clean_text = word_tokenize(text)
        text_result = re.sub(r"[,@\'?\.$%_]", "", text, flags=re.I)

        return {'result': rext_result}
        
