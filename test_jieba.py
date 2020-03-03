# coding:utf-8
import jieba.posseg as pseg
import time
import jieba
import pandas as pd
import os

start_time = time.time()
sentence = pseg.cut('刘德华唱的歌')
end_time = time.time()
for w in sentence:
    print (w.word,w.flag)

print('分词 Took %f second' % (end_time - start_time))


# 读取jieba词库，生成词性标注表，保存为excel
# jieba_dict = os.path.dirname(jieba.__file__) + '/dict.txt'
# df_jieba = pd.read_table(jieba_dict, sep=' ', header=None)[[2, 0]]
# dt = {k: set() for k in df_jieba[2].values}
# for f, w in df_jieba.values:
#     dt[f].add(w)
# ls_of_ls = [(f, ' '.join(list(w)[:50])) for f, w in dt.items()]
# pd.DataFrame(ls_of_ls, columns=['flag', 'words']).sort_values('flag').to_excel('flag.xlsx', index=None)
