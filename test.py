import nltk
import re
import html2text
import os
import requests
sample=open("//Users/xyang/Downloads/CommonCrawl-sample-2.warc","rb")
f=open("//Users/xyang/Downloads/extract.txt","w")

def extract_entity_names(t):
    entity_names = []
    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
    return entity_names

w_tag=0
h_tag=0
n=0
for string in sample:
    record1=string.decode('utf-8')
    record=str(record1)
    data={'uuid':[],'entity':[],'sentences':[],'result':[],'wiki':[]}
    if w_tag==0:
        if re.findall(r"WARC-Type: respon(.+?)e",record):
            w_tag=w_tag+1
    elif w_tag==1:
        w_tag=w_tag+1
    elif w_tag==2:
        if re.findall(r"WARC-Record-ID: <urn:(.+?)>",record):
            uuid=re.findall(r"WARC-Record-ID: <urn:(.+?)>",record)
        else:
            if h_tag==0:
                if re.findall(r"<body(.+?)",record):
                    h_tag=1
            if h_tag==1:
                if re.findall(r"(.+?)/body>",record):
                    h_tag=0
                    w_tag=0
                else:
                    s=html2text.html2text(record)
                    sentences = nltk.sent_tokenize(s)
                    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
                    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
                    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)
                    entity_names = []
                    for tree in chunked_sentences:
                        entity_names.extend(extract_entity_names(tree))
                    if entity_names:
                        if tagged_sentences:
                            for uid in uuid:
                                data['uuid'].append(uid)
                            for ename in entity_names:
                                data['entity'].append(ename)
                            count=0
                            for each in tagged_sentences:
                                data['sentences'].append(each)
                                count=count+1
                            # for e in entity_names:
                                # resfree=os.popen('curl "http://10.149.0.127:9200/freebase/label/_search?q=%s"'%e).read()
                                # data['result'].append(resfree)
                                # r=requests.get('https://en.wikipedia.org/wiki/%s'%e)
                                # for li in r:
                                #     #line1=li.decode('utf-8')
                                #     line=str(li)
                                #     if re.findall(r"<p(.+?)</p>", line):
                                #         h=html2text.html2text(line)
                                #         if h:
                                #             print(h)
                                #             data['wiki'].append(h)
                            # print data
                            f.write(str(data))
            else:
                pass
    else:
        pass