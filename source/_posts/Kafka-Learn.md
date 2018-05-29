---
title: Kafka 使用入门
date: 2018-05-29 13:57:07
categories: 编程语言
tags:
  - python
---

<!-- 文章开头都用它了，整齐才好看 -->
{% note default %}
统计信息数据量较大，感觉用 kafka 会比较合适，临时学一下
{% endnote %}

<!--more-->

---

# 参考
http://dblab.xmu.edu.cn/blog/1096-2/

# kafka 安装与测试
## 下载 kafka
```
wget --no-check-certificate http://mirror.bit.edu.cn/apache/kafka/1.1.0/kafka_2.11-1.1.0.tgz
```

## 安装
```
tar -xzf kafka_2.11-1.1.0.tgz -C /usr/local
cd /usr/local
mv kafka_2.11-1.1.0 kafka
```

## 测试数据准备
```
wget --no-check-certificate http://download.tensorflow.org/data/iris_training.csv
```

## 测试
* 启动 zookeeper
```
cd /usr/local/kafka
bin/zookeeper-server-start.sh config/zookeeper.properties
```
* 启动 kafka
```
cd /usr/local/kafka
bin/kafka-server-start.sh config/server.properties
```
* 创建 topic
```
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic dblab
```
* 查看 topic
```
bin/kafka-topics.sh --list --zookeeper localhost:2181
```
* 生产数据
```
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic dblab
```
* 输入任意数据
```
hello hadoop
hello xmu
hadoop world
```
* 查看数据
```
bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic dblab --from-beginning
```

# python 操作 kafka 示例
## 生产者代码
```python
from kafka import KafkaConsumer

consumer = KafkaConsumer('sex')
for msg in consumer:
    print((msg.value).decode('utf8'))
```

## 消费者代码
```python
# coding: utf-8
import csv
import time
from kafka import KafkaProducer

# 实例化一个 KafkaProducer 示例，用于向 Kafka 投递消息
producer = KafkaProducer(bootstrap_servers='localhost:9092')
# 打开数据文件
csvfile = open("./iris_training.csv","r")
# 生成一个可用于读取 csv 文件的 reader
reader = csv.reader(csvfile)

for line in reader:
    gender = line[4] # 性别在每行日志代码的第 9 个元素
    if gender == 'virginica':
        continue # 去除第一行表头
    time.sleep(0.1) # 每隔 0.1 秒发送一行数据
    # 发送数据，topic 为'sex'
    producer.send('sex',line[4].encode('utf8'))
```
