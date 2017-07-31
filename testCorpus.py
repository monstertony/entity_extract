# -*- coding: utf-8 -*-
__author__ = 'xyang'

import os
from gensim import utils
from gensim.models.doc2vec import LabeledSentence
import json
import sys
from gensim.models import Doc2Vec
reload(sys)
sys.setdefaultencoding('utf-8')
rootDir = '/Users/xyang/Downloads/allcorpus'
savefilepath='/Users/xyang/Downloads/all.txt'
c=open(savefilepath,'a')
n=0
for list in os.listdir(rootDir):
    if list=='.DS_Store':
        continue
    else:
        path = os.path.join(rootDir, list)
        print path
        for file in os.listdir(path):
            if file=='.DS_Store':
                continue
            else:
                n=n+1
                file = os.path.join(path, file)
                f=[]
                f=json.load(open(file, 'r'))
                # f.encode('utf-8')
                c.write(f['body'])
                # print f[]
                print file

print n
# data=[]
# data=json.load(open(rootDir,'r'))
# print data['body']