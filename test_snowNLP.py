# coding:utf-8
import time
from snownlp import SnowNLP

start_time = time.time()
s = SnowNLP('我想听张靓颖的这就是爱情')
end_time = time.time()
print('分词结果：', s.words)

print('词性标注结果：')
for each in s.tags:
    print(each)

print('分词+词性标注 Took %f second' % (end_time - start_time))
