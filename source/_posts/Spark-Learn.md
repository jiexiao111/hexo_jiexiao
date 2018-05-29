---
title: Spark 入门
date: 2018-05-29 17:24:46
categories: 编程语言
tags:
  - python
---

<!-- 文章开头都用它了，整齐才好看 -->
{% note default %}
统计信息数据量较大，为了后期方便扩展，直接使用 spark 进行处理
{% endnote %}

<!--more-->

---

# 参考
http://dblab.xmu.edu.cn/blog/1709-2/
http://dblab.xmu.edu.cn/blog/1358-2/

# 安装
## 安装 hadoop
### 参考
http://dblab.xmu.edu.cn/blog/install-hadoop-simplify/
http://dblab.xmu.edu.cn/blog/install-hadoop/
### 准备
```
apt-get install -y rsync ssh
```
### 创建 Hadoop 用户
```
sudo useradd -m hadoop -s /bin/bash     # 创建 hadoop 用户
sudo passwd hadoop          # 修改密码
sudo adduser hadoop sudo    # 增加管理员权限
su hadoop # 登陆 hadoop 用户
```
### 更新源
```
sudo apt-get update
```
### 配置无密码登陆
```
sudo apt-get install openssh-server
cd ~
mkdir .ssh                  # 可能该文件已存在，不影响
cd ~/.ssh/
ssh-keygen -t rsa           # 会有提示，都按回车就可以
cat id_rsa.pub >> authorized_keys  # 加入授权
```
### 安装 java
这一步我已经安装了 java1.8，貌似无法降级安装，先尝试使用 1.8，所以没有使用以下命令
```
apt-get install -y openjdk-7-jre openjdk-7-jdk
```
### 配置变量（~/.bashrc）
既然都用了 java8 了索性用最新的 hadoop，需要注意这行配置要放在 .bashrc 最前面
教程提供的参数
```
export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64
```
实际使用的参数
```
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```
### 下载 hadoop
```
wget http://www-eu.apache.org/dist/hadoop/common/hadoop-3.1.0/hadoop-3.1.0.tar.gz
sudo tar -zxvf hadoop-3.1.0.tar.gz -C /usr/local/
sudo mv ./hadoop-3.1.0 hadoop
sudo chown -R hadoop ./hadoop
```
### 修改配置文件
修改配置文件 core-site.xml (vim /usr/local/hadoop/etc/hadoop/core-site.xml)：
```
<configuration>
	<property>
		<name>hadoop.tmp.dir</name>
		<value>file:/usr/local/hadoop/tmp</value>
		<description>Abase for other temporary directories.</description>
	</property>
	<property>
		<name>fs.defaultFS</name>
		<value>hdfs://localhost:9000</value>
	</property>
</configuration>
```
修改配置文件 hdfs-site.xml：
```
<configuration>
	<property>
		<name>dfs.replication</name>
		<value>1</value>
	</property>
	<property>
		<name>dfs.namenode.name.dir</name>
		<value>file:/usr/local/hadoop/tmp/dfs/name</value>
	</property>
	<property>
		<name>dfs.datanode.data.dir</name>
		<value>file:/usr/local/hadoop/tmp/dfs/data</value>
	</property>
</configuration>
```
### 启动 Hadoop
```
cd /usr/local/hadoop
bin/hdfs namenode -format       # namenode 格式化
sbin/start-dfs.sh               # 开启守护进程
jps                             # 判断是否启动成功
```
若成功启动则会列出如下进程：NameNode、DataNode 和 SecondaryNameNode
### 运行 wordcount 实例
```
bin/hdfs dfs -mkdir -p /user/hadoop     # 创建 HDFS 目录
bin/hdfs dfs -mkdir input
bin/hdfs dfs -put etc/hadoop/*.xml input  # 将配置文件作为输入
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar grep input output 'dfs[a-z.]+'
bin/hdfs dfs -cat output/*                # 查看输出
```
## 安装 Spark
### 下载并安装
```
su hadoop
wget --no-check-certificate https://archive.apache.org/dist/spark/spark-2.3.0/spark-2.3.0-bin-without-hadoop.tgz
tar -zxf spark-2.3.0-bin-without-hadoop.tgz.2 -C /usr/local
cd /usr/local
mv spark-2.3.0-bin-without-hadoop spark
sudo chown -R hadoop:hadoop ./spark          # 此处的 hadoop 为你的用户名
```
### 编辑配置文件
* 复制配置文件模板
```
cd /usr/local/spark
cp ./conf/spark-env.sh.template ./conf/spark-env.sh
```
* 编辑 spark-env.sh 文件 (vim ./conf/spark-env.sh)，在第一行添加以下配置信息向 .bashrc 添加以下配置
```
export SPARK_DIST_CLASSPATH=$(/usr/local/hadoop/bin/hadoop classpath)
export HADOOP_HOME=/usr/local/hadoop
export SPARK_HOME=/usr/local/spark
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$PYTHONPATH
export PYSPARK_PYTHON=python3
export PATH=$HADOOP_HOME/bin:$SPARK_HOME/bin:$PATH
```
### 测试
```
bin/run-example SparkPi 2>&1 | grep "Pi is"
```
### 交互式操作
```
bin/pyspark
8 * 2 + 5
```
### python 操作 spark
* 安装 pyspark
```
pip install pypandoc
pip install pyspark
```
* 测试代码
```
from pyspark import SparkContext
sc = SparkContext( 'local', 'test')
logFile = "file:///usr/local/spark/README.md"
logData = sc.textFile(logFile, 2).cache()
numAs = logData.filter(lambda line: 'a' in line).count()
numBs = logData.filter(lambda line: 'b' in line).count()
print('Lines with a: %s, Lines with b: %s' % (numAs, numBs))
```
* 测试结果
```
Lines with a: 61, Lines with b: 30
```

