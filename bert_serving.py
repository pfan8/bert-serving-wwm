'''
pip下载bert-serving的server和client之后，启动server：

bert-serving-start -model_dir chinese_L-12_H-768_A-12/(预训练模型) -num_worker=2

'''
from bert_serving.client import BertClient
from tqdm import tqdm
import pickle

bc = BertClient(ip='localhost')

data = []
file = 'baidu_95.csv' # 语料
with open(file, 'r', encoding='utf8') as f:
	for line in tqdm(f.readlines()):
		words = line.split(' ')
		data.append(bc.encode(words))

save_path = 'bert_serving_vector.pkl'
with open(save_path, 'wb') as f:
	pickle.dump(data, f)

print('successful get vocab at {}'.format(save_path))
