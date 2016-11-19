from nltk.stem import PorterStemmer
from nltk.tokenize import SpaceTokenizer
from nltk.corpus import stopwords
from functools import partial
from gensim import corpora
from gensim.models import TfidfModel
import re

tokenizer = SpaceTokenizer()
stemmer = PorterStemmer()

pipeline = [
            lambda s: re.sub('<[^>]*>', ' ', s),
            lambda s: re.sub('[^\w\s]', '', s),
            lambda s: re.sub('[\d]', '', s),
            lambda s: s.lower(),
            lambda s: ' '.join(filter(lambda s: not (s in stopwords.words()), tokenizer.tokenize(s))),
            lambda s: ' '.join(map(lambda t: stemmer.stem(t), tokenizer.tokenize(s)))
           ]

def preprocess_text(text, pipeline=pipeline):
    if len(pipeline) == 0:
        return text
    else:
        return preprocess_text(pipeline[0](text), pipeline[1:])
