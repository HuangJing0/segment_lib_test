# coding:utf-8

import pynlpir
import time
# 打开分词器
pynlpir.open()


text1 = "刘德华唱的歌"

start_time = time.time()
# 分词，默认打开分词和词性标注功能
test1 = pynlpir.segment(text1)
end_time = time.time()
print(test1)
print('分词+词性标注 Took %f second' % (end_time - start_time))


# #将词性标注语言变更为汉语
# test2 = pynlpir.segment(text1,pos_english=False)
# print('2.汉语标注模式:\n' + str(test2))
#
#
# #关闭词性标注
# test3 = pynlpir.segment(text1,pos_tagging=False)
# print('3.无词性标注模式:\n' + str(test3))