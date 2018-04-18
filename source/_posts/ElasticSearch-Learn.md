---
title: ElasticSearch 简单使用
date: 2018-04-16 21:26:40
categories: 数据库
tags:
  - ElasticSearch
---

{% note default %}
ElasticSearch 使用记录
{% endnote %}

<!--more-->

---

# 相关资料
官方指导
https://www.elastic.co/downloads/elasticsearch
https://www.elastic.co/guide/en/elasticsearch/reference/current/zip-targz.html

中文指南
https://es.xiaoleilu.com/010_Intro/15_API.html

入门博客
http://www.ruanyifeng.com/blog/2017/08/elasticsearch.html
https://segmentfault.com/a/1190000011661882]

不同搜索模式入门
https://marcobonzanini.com/2015/02/09/phrase-match-and-proximity-search-in-elasticsearch/

# 安装
```
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.3.tar.gz --no-check-certificate
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.3.tar.gz.sha512 --no-check-certificate
shasum -a 512 -c elasticsearch-6.2.3.tar.gz.sha512
tar -xzf elasticsearch-6.2.3.tar.gz
cd elasticsearch-6.2.3/
```

创建 elsearch 用户组及 elsearch 用户
```
groupadd elsearch
useradd elsearch -g elsearch -p elasticsearch
```

更改 elasticsearch-6.2.3 文件夹及内部文件的所属用户及组为 elsearch:elsearch
```
chown -R elsearch:elsearch elasticsearch-6.2.3
```

# 启动
切换到 elsearch 用户再启动
```
su elsearch
cd elasticsearch/bin
./elasticsearch
```

启动后打印信息如下
```
[2015-12-30 10:15:44,876][WARN ][bootstrap                ] unable to install syscall filter: prctl(PR_GET_NO_NEW_PRIVS): Invalid argument
[2015-12-30 10:15:45,175][INFO ][node                     ] [Grim Hunter] version[2.1.1], pid[26383], build[40e2c53/2015-12-15T13:05:55Z]
[2015-12-30 10:15:45,176][INFO ][node                     ] [Grim Hunter] initializing ...
[2015-12-30 10:15:45,243][INFO ][plugins                  ] [Grim Hunter] loaded [], sites []
[2015-12-30 10:15:45,272][INFO ][env                      ] [Grim Hunter] using [1] data paths, mounts [[/ (/dev/mapper/vg_yong-lv_root)]], net usable_space [33.3gb], net total_space [49gb], spins? [no], types [ext4]
[2015-12-30 10:15:47,318][INFO ][node                     ] [Grim Hunter] initialized
[2015-12-30 10:15:47,318][INFO ][node                     ] [Grim Hunter] starting ...
[2015-12-30 10:15:47,388][INFO ][discovery                ] [Grim Hunter] elasticsearch/fnXUCLOQQBiC1aR7hhB82Q
[2015-12-30 10:15:50,442][INFO ][cluster.service          ] [Grim Hunter] new_master {Grim Hunter}{fnXUCLOQQBiC1aR7hhB82Q}{127.0.0.1}{127.0.0.1:9300}, reason: zen-disco-join(elected_as_master, [0] joins received)
[2015-12-30 10:15:50,491][INFO ][node                     ] [Grim Hunter] started
[2015-12-30 10:15:50,526][INFO ][gateway                  ] [Grim Hunter] recovered [0] indices into cluster_state
```

后端启动
```
./elasticsearch -d
```

# 测试
打开另一个终端进行测试：
```
curl 'http://localhost:9200/?pretty'
```

你能看到以下返回信息，如果返回信息有误查看是否因为 curl 配置了代理导致访问错误
```
{
   "status": 200,
   "name": "Shrunken Bones",
   "version": {
      "number": "1.4.0",
      "lucene_version": "4.10"
   },
   "tagline": "You Know, for Search"
}
```

# 使用
新建和删除 Index
新建 Index，可以直接向 Elastic 服务器发出 PUT 请求。下面的例子是新建一个名叫 weather 的 Index。
```
$ curl -X PUT 'localhost:9200/weather'
```

服务器返回一个 JSON 对象，里面的 acknowledged 字段表示操作成功。
```
{
  "acknowledged":true,
  "shards_acknowledged":true
}
```

然后，我们发出 DELETE 请求，删除这个 Index。
```
$ curl -X DELETE 'localhost:9200/weather'
```

新增记录
```
$ curl -H "Content-Type: application/json" -X PUT 'localhost:9200/accounts/person/1' -d '
{
  "user": "jiexiao",
  "title": "1",
  "desc": "This is a brown fox"
}'

$ curl -H "Content-Type: application/json" -X PUT 'localhost:9200/accounts/person/2' -d '
{
  "user": "jiexiao",
  "title": "2",
  "desc": "This is a brown dog"
}'

$ curl -H "Content-Type: application/json" -X PUT 'localhost:9200/accounts/person/3' -d '
{
  "user": "jiexiao",
  "title": "3",
  "desc": "This dog is really brown"
}'

$ curl -H "Content-Type: application/json" -X PUT 'localhost:9200/accounts/person/4' -d '
{
  "user": "jiexiao",
  "title": "4",
  "desc": "The dog is brown but this document is very very long"
}'

$ curl -H "Content-Type: application/json" -X PUT 'localhost:9200/accounts/person/5' -d '
{
  "user": "jiexiao",
  "title": "5",
  "desc": "There is also a white cat"
}'

$ curl -H "Content-Type: application/json" -X PUT 'localhost:9200/accounts/person/6' -d '
{
  "user": "jiexiao",
  "title": "6",
  "desc": "The quick brown fox jumps over the lazy dog"
}'

$ curl -H "Content-Type: application/json" -X PUT 'localhost:9200/accounts/person/7' -d '
{
  "user": "jiexiao",
  "title": "7",
  "desc": "This is a brown [ ] dog"
}'

$ curl -H "Content-Type: application/json" -X PUT 'localhost:9200/accounts/person/8' -d '
{
  "user": "jiexiao",
  "title": "8",
  "desc": "This is a Brown Dog"
}'
```

根据 /Index/Type/Id 查询记录
```
$ curl 'localhost:9200/accounts/person/1?pretty=true'
{
  "_index" : "accounts",
  "_type" : "person",
  "_id" : "1",
  "_version" : 1,
  "found" : true,
  "_source" : {
    "user" : "jiexiao",
    "title" : "1",
    "desc" : "This is a brown fox"
  }
}
```

返回所有记录
```
curl 'localhost:9200/accounts/person/_search'
```

全文搜索
```
curl -H "Content-Type: application/json" 'localhost:9200/accounts/person/_search'  -d '
{
  "query" : { "match" : { "desc" : {"query": "quick brown dog tangting"}}}
}'
```

搜索词组
```
curl -H "Content-Type: application/json" 'localhost:9200/accounts/person/_search'  -d '
{
  "query" : { "match_phrase" : { "desc" : {"query": "brown  dog", "slop": 3}}}
}'
```

可以发现 ES 不支持特殊符号
```
curl -H "Content-Type: application/json" 'localhost:9200/accounts/person/_search'  -d '
{
  "query" : { "match_phrase" : { "desc" : {"query": "[ ]", "slop": 3}}}
}'
```

对比发现 ES 不区分大小写
```
curl -H "Content-Type: application/json" 'localhost:9200/accounts/person/_search'  -d '
{
  "query" : { "match_phrase" : { "desc" : {"query": "Brown  Dog", "slop": 3}}}
}'
```

测试分词
```
curl -X GET "http://localhost:9200/_analyze" -H 'Content-Type: application/json' -d'
{
  "analyzer" : "standard",
  "text" : "this_is a testapple 揭晓"
}'
```

可以看到``this_is``、``testapple``没有被切分，而``揭晓``被切分了
```
{
  "tokens": [
    {
      "token": "this_is",
      "start_offset": 0,
      "end_offset": 7,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "a",
      "start_offset": 8,
      "end_offset": 9,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "testapple",
      "start_offset": 10,
      "end_offset": 19,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "揭",
      "start_offset": 20,
      "end_offset": 21,
      "type": "<IDEOGRAPHIC>",
      "position": 3
    },
    {
      "token": "晓",
      "start_offset": 21,
      "end_offset": 22,
      "type": "<IDEOGRAPHIC>",
      "position": 4
    }
  ]
}
```

## 增量同步 mysql
利用插件还是不靠谱，自己写代码比较放心

https://blog.csdn.net/yeyuma/article/details/50240595#quote

安装 logstash 参考 https://www.digitalocean.com/community/tutorials/how-to-install-elasticsearch-logstash-and-kibana-elk-stack-on-ubuntu-14-04#install-logstash
```
echo 'deb http://packages.elastic.co/logstash/2.2/debian stable main' | sudo tee /etc/apt/sources.list.d/logstash-2.2.x.list
apt-get update
apt-get install logstash
```

update 时出现错误
```
W: GPG error: http://packages.elastic.co/logstash/2.2/debian stable Release: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY D27D666CD88E42B4
```

解决办法，执行之前配置一下全局代理
```
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys D27D666CD88E42B4
```

安装 gem
```
apt-get install gem
```

安装 logstash-input-jdbc，记得配置全局代理
```
/opt/logstash/bin/plugin install logstash-input-jdbc
```

## python 实现 mysql 同步
