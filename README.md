# Redips分布式爬虫系统
本项目的 **设计文档** 及 **需求文档** 位于项目文件的docs目录中。

↓↓↓↓↓↓↓↓↓↓↓↓**请观看演示视频**↓↓↓↓↓↓↓↓↓↓↓↓↓
[http://www.bilibili.com/video/av11721506/](http://www.bilibili.com/video/av11721506/)
↑↑↑↑↑↑↑↑↑↑↑↑**请观看演示视频**↑↑↑↑↑↑↑↑↑↑↑↑↑

## 0.Redips介绍
Redips是一个基于Scrapy框架实现的分布式爬虫系统。

- 项目名称"redips"是取自单词爬虫"spider"的反向拼写，意在强调我们的爬虫系统可以顺利解决反爬问题，同时也向实现分布式的核心组件：Redis内存数据库致敬。
- Redips通过redis内存数据库器实现了分布式爬虫的优势，并且达成了优化算法、设计更全的逻辑，实现采集高效、优化内存、数据准确、用户操作便捷的目标，以满足广大电商数据需求者的需要。
- 前端Web页面使用Bootstrap模板搭建。
- 后端通过php控制scrapyd服务器，调用部署好的爬虫

## 1.Docker封装的爬虫系统功能模块
- Web端：[http://redipstest.t2.daoapp.io:61027/](http://redipstest.t2.daoapp.io:61027/)
- 爬虫服务器端：[http://redips-scrapydtest.t2.daoapp.io:61031/](http://redips-scrapydtest.t2.daoapp.io:61031/)

## 2.简要操作说明
1. 打开爬虫服务器端
2. 打开Redips系统Web端页面
3. 运行爬虫
4. 运行后爬虫服务器端可查看运行状态及日志，Web端可查看数据库内容

## 3.前端操作
- 各类爬虫均从网页主界面左侧菜单栏【Navigation-XX-相应种类爬取】中进入
- 在子界面中，先输入参数配置，点击【Submit】进行表单的提交（【Reset】按键即可重置为默认值）
- 接着点击【Start】开启爬虫工作
- 随时可以点击【Check】查看当前爬虫所有工作的状态
- 【Stop】按键即可停止爬虫工作
- 请在【爬取结果】中查看对应的爬取内容

## 4.需求环境
- 操作系统：Linux
- 依赖包：Python 2.7, Scrapy 1.3.3, Scrapyd, Scrapyd-client, Scrapy-Redis, MySQL, apache
- 我们使用的是自己修改后的Scrapy-Redis组件，位于项目中的/lib/scrapy_redis目录，直接通过覆盖Python2.7的scrapy_redis

```
scrapy安装命令：
sudo apt-get install python-dev
sudo apt-get install libevent-dev
apt-get install python-pip
pip install Scrapy
```

```
scrapyd安装命令：
apt-get install scrapyd
```

```
scrapyd-client安装命令：
apt-get install scrapyd-client
```

```
mysql安装命令：
sudo apt-get install mysql-server mysql-client
```

```
apache安装命令：
sudo apt-get install apache2
```

```
php安装命令：
sudo apt-get install libapache2-mod-php php
sudo apt-get install php-gd
sudo apt-get install php-mysql
```

## 5.文件结构
Redips
│  deploy.sh                          # 部署用脚本文件
│  README.md
│
├─docs                                # **文档目录**
│      **设计文档.pdf**
│      **需求文档.pdf**
├─lib
│  └─scrapy_redis                     # **修改后的分布式组件**
│
├─projects                            # **爬虫项目目录**
│  ├─bodyExtract                      # 正文提取
│  ├─DoubanBookSpider                 # 豆瓣图书
│  ├─JDSearch                         # 京东搜索
│  ├─jingdongModel                    # 京东模板
│  ├─ProxyCrawler                     # 代理爬取器
│  ├─ProxyTester                      # 代理测试器
│  ├─taobaoCrawler                    # 淘宝全站
│  ├─taobaoSearch                     # 淘宝搜索
│  ├─yhdCrawler                       # 一号店全站
│  └─yhdSearch                        # 一号店搜索
│
└─web
    │  index.html                     # Web主页
    │
    ├─page                            # 页面
    │  │  1hdall.html                 # 一号店全网爬取页面
    │  │  1hdsearch.html              # 一号店搜索爬取页面
    │  │  boke.html                   # 正文提取页面
    │  │  douban.html                 # 豆瓣图书爬取页面
    │  │  jdmodel.html                # 京东模板爬取页面
    │  │  jdsearch.html               # 京东搜索爬取页面
    │  │  tball.html                  # 淘宝全网搜索页面
    │  │  tbsearch.html               # 淘宝搜索爬取页面
    │  │
    │  └─assets                       # css/js/image目录
    │
    └─php                             # php文件目录
