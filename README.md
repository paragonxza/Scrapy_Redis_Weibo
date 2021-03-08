# 微博爬虫启用方式

在当前目录输入**pip install -r requirements.txt**

在当前目录输入**scrapy crawl weibocn** 

即可在redis/mongodb可视化界面看到相关数据信息

**以下为可选scrapyd部署：**

- 在cmd/terminal输入**(scrapyd> ~/scrapyd.log &)**开启scrapyd服务
- 在当前目录输入**scrapyd-deploy**部署爬虫项目
- 输入**curl http://ipaddress:6800/schedule.json -d project=weibo -d spider=weibocn**远端启动

# bloomfilter配置

## 安装

输入以下命令:

```python
pip install scrapy-redis-bloomfilter
```

## 使用

在settings.py 里添加如下代码：

```python
# Persist
SCHEDULER_PERSIST = True
# Ensure use this Scheduler
SCHEDULER = "scrapy_redis_bloomfilter.scheduler.Scheduler"
# 去重类，要使用 BloomFilter 请替换 DUPEFILTER_CLASS
DUPEFILTER_CLASS = "scrapy_redis_bloomfilter.dupefilter.RFPDupeFilter"
# 哈希函数的个数，默认为 6，可以自行修改
BLOOMFILTER_HASH_NUMBER = 6
# BloomFilter 的 bit 参数，默认 30，占用 128MB 空间，去重量级 1 亿
BLOOMFILTER_BIT = 30
# redis连接
REDIS_URL = 'redis://username:password6@ipaddress:6379'
```

# 配置随机user-agent

在settings.py 的 DOWNLOADER_MIDDLEWARES里添加如下两行代码：

```python
# random user-agent
'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
```

