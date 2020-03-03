# coding:utf-8
from stanfordcorenlp import StanfordCoreNLP
import time

start_time = time.time()
nlp = StanfordCoreNLP(path_or_host='/Users/jing/opt/stanford-corenlp-full-2018-10-05', lang='zh')
end_time = time.time()
print('加载模型 Took %f second' % (end_time - start_time))
sentence = '有没有新出的电视剧'

start_time = time.time()
word = nlp.word_tokenize(sentence)
end_time = time.time()
print(word)
print('分词 Took %f second' % (end_time - start_time))

start_time = time.time()
tager = nlp.pos_tag(sentence)
end_time = time.time()
print(tager)
print('词性标注 Took %f second' % (end_time - start_time))

start_time = time.time()
parse = nlp.dependency_parse(sentence)
end_time = time.time()
print(parse)
print('依存分析 Took %f second' % (end_time - start_time))