from flask_restful import Resource, reqparse
import nltk
from nltk.tokenize import sent_tokenize
tokenizer = nltk.RegexpTokenizer(r"\w+")

# CLASS DESCRIPTION:
    # Devides and clears the sentence of punctuation marks and builds a dependency tree on each sentence
    # Allocates its own names and verbs
    # added: Temuri Kitoshvili

class Chunk_CleanSentences(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('text',
                        type=str,
                        required=True,
                        help="გთხოვთ შეიყვანოთ სწორი წინადადება")

    def get(self):
        data = Chunk_CleanSentences.parser.parse_args()
        text = data['text']

        sentences = sent_tokenize(text)
        clean_sentences = []

        for sent in sentences:
            clear_sentence = tokenizer.tokenize(sent)
            clean_sentences.append(clear_sentence)

        for word in clean_sentences:
            tagged_sent = nltk.pos_tag(word)
            chunkGram = r"""Chunk: {<VB.?>*<NNP>?} """
            chuckParser = nltk.RegexpParser(chunkGram)
            chunked = chuckParser.parse(tagged_sent)

            chunked.draw()

        return {"clean_sentences": clean_sentences}

