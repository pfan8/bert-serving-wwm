# bert-serving-wwm
bert-serving部署，使用哈工大[bert-wwm](https://github.com/ymcui/Chinese-BERT-wwm)预训练模型

[模型下载地址](https://drive.google.com/file/d/1RoTQsXp2hkQ1gSRVylRIJfQxJUgkfJMW/view)

## 使用方式

1. pip安装
```shell
pip install bert-serving-server
pip install bert-serving-client
```

2. 启动server
```shell
bert-serving-start -model_dir chinese_L-12_H-768_A-12/(预训练模型) -num_worker=2(线程数量，可酌情增减)
```

3. client调用服务

启动脚本bert-serving.py即可，可在文件中修改语料位置和vocab保存位置
