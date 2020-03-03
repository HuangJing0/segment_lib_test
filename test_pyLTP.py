# coding:utf-8
import os
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import Parser

import time


start_time = time.time()
LTP_DATA_DIR = '/Users/jing/opt/ltp_data_v3.4.0'
cws_model_path = os.path.join(LTP_DATA_DIR,'cws.model')
segmentor = Segmentor()
segmentor.load(cws_model_path)
words = segmentor.segment('刘德华唱的歌')
end_time = time.time()
print('\t'.join(words))
print('分词 Took %f second' % (end_time - start_time))
segmentor.release()

start_time = time.time()
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
postagger = Postagger() # 初始化实例
postagger.load(pos_model_path)  # 加载模型
postags = postagger.postag(words)  # 词性标注
end_time = time.time()
print('\t'.join(postags))
print('词性标注 Took %f second' % (end_time - start_time))
postagger.release()  # 释放模型


start_time = time.time()
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`
parser = Parser() # 初始化实例
parser.load(par_model_path)  # 加载模型
arcs = parser.parse(words, postags)  # 句法分析
end_time = time.time()
print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
print('依存分析 Took %f second' % (end_time - start_time))
parser.release()  # 释放模型


