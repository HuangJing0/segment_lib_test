# coding:utf-8

import time
import thulac


thu1 = thulac.thulac()
start_time = time.time()
text = thu1.cut("刘德华唱的歌", text=True)
end_time = time.time()
print(text)
print('分词+词性标注 Took %f second' % (end_time - start_time))