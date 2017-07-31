__author__ = 'xyang'

# gensim modules
from gensim import utils
from gensim.models.doc2vec import LabeledSentence
from gensim.models import Doc2Vec

# numpy
import numpy

# random
from random import shuffle

# classifier
from sklearn.linear_model import LogisticRegression

class LabeledLineSentence(object):
    def __init__(self, sources):
        self.sources = sources

        flipped = {}

        # make sure that keys are unique
        for key, value in sources.items():
            if value not in flipped:
                flipped[value] = [key]
            else:
                raise Exception('Non-unique prefix encountered')

    def __iter__(self):
        for source, prefix in self.sources.items():
            with utils.smart_open(source) as fin:
                for item_no, line in enumerate(fin):
                    try:
                        yield LabeledSentence(utils.to_unicode(line).split(), [prefix + '_%s' % item_no])
                    except:
                        continue

    def to_array(self):
        self.sentences = []
        for source, prefix in self.sources.items():
            with utils.smart_open(source) as fin:
                for item_no, line in enumerate(fin):
                    try:
                        self.sentences.append(LabeledSentence(utils.to_unicode(line).split(), [prefix + '_%s' % item_no]))
                    except:
                        continue

        return self.sentences

    def sentences_perm(self):
        shuffle(self.sentences)
        return self.sentences

sources = {'/Users/xyang/Downloads/rt-polaritydata/rt-polaritydata/rt-polarityneg.txt':'TEST_NEG', '/Users/xyang/Downloads/rt-polaritydata/rt-polaritydata/rt-polaritypos.txt':'TEST_POS'}

sentences = LabeledLineSentence(sources)

model = Doc2Vec(min_count=1, window=10, size=100, sample=1e-4, negative=5, workers=8)

model.build_vocab(sentences.to_array())

for epoch in range(10):
    model.train(sentences.sentences_perm())

# model.save('./imdb.d2v')
#
# model = Doc2Vec.load('./imdb.d2v')

m=model.most_similar('bad')
print m
