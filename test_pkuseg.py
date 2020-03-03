# coding:utf-8

import pkuseg
import time


seg = pkuseg.pkuseg(postag=True)
start_time = time.time()
text = seg.cut('我想听张靓颖的这就是爱情')  # 进行分词
end_time = time.time()
print(text)
print('分词+词性标注 Took %f second' % (end_time - start_time))
