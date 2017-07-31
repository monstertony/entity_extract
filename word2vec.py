from gensim.models import word2vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus("/Users/xyang/Downloads/text8")
model=word2vec.Word2Vec().load("/Users/xyang/Downloads/word2vec-sentiments-master/imdb.d2v");
# model=word2vec.Word2Vec.load("/Users/xyang/Downloads/word2vec-sentiments-master/imdb.d2v")
# model.load("/Users/xyang/Downloads/word2vec-sentiments-master/imdb.d2v")
# model=word2vec.Word2Vec(sentences)
# model.train(sentences)
s=model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
m=model.doesnt_match("bad good juice".split())
# model.load("/Users/xyang/Downloads/word2vec-sentiments-master/imdb.d2v")
# model.save("/Users/xyang/Downloads/word2vec-sentiments-master/imdb.d2v")
print s
print m