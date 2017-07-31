__author__ = 'xyang'

from gensim import utils
from gensim.models.doc2vec import LabeledSentence
from gensim.models import Doc2Vec
import math
import os
import json
import nltk
import sys
import csv
reload(sys)
sys.setdefaultencoding('utf-8')
rootDir = '/Users/xyang/Downloads/non_corpus'

model = Doc2Vec.load('/Users/xyang/Downloads/corpus_8.d2v')
n=0

output='/Users/xyang/Downloads/non_con.csv'
csvfile=file(output,'w')
writer=csv.writer(csvfile,delimiter=',')
for list in os.listdir(rootDir):
    # print list
    if list=='.DS_Store':
        continue
    else:
        path = os.path.join(rootDir, list)
        for file in os.listdir(path):
            if file=='.DS_Store':
                continue
            else:
                f=os.path.join(path,file)
                print f
                data=[]
                data=json.load(open(f,'r'))
                p=model.infer_vector(data['body'])
                print p
                f=[]
                f.append(str(file))
                for each in p:
                    f.append(str(each))
                writer.writerows([f])
        # with open(output,'w') as csvfile:
        #     writer=csv.writer(csvfile,delimiter=',')
        #     for file in os.listdir(path):
        #         if file=='.DS_Store':
        #             continue
        #         else:
        #             f=os.path.join(path,file)
        #             print f
        #             data=[]
        #             data=json.load(open(f,'r'))
        #             p=model.infer_vector(data['body'])
        #             print p
        #             f=[]
        #             f.append(str(file))
        #             for each in p:
        #                 f.append(str(each))
        #             writer.writerows([f])