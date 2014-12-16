#!/usr/bin/env python
#coding:utf-8

import os, sys
import time
import sys
import pycurl

URL = "http://maikaiheng.info/"    # 探测的目标URL
c = pycurl.Curl()    # 创建一个Curl对象
c.setopt(pycurl.URL, URL)    # 定义请求的URL常量

c.setopt(pycurl.CONNECTTIMEOUT, 5)    # 定义连接超时时间

c.setopt(pycurl.TIMEOUT, 5)    # 定义下载超时时间
c.setopt(pycurl.NOPROGRESS, 1)    # 屏蔽下载进度条
c.setopt(pycurl.FORBID_REUSE, 1)    # 完成交互后强制断开连接，不重用
c.setopt(pycurl.MAXREDIRS, 1)    # 指定HTTP重定向的最大连接数为1
c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)    # 设置保存DNS信息的时间为30秒

# 创建一个文件对象，以"wb"方式打开，用来存储返回的http头部及页面内容
indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt", "wb")
c.setopt(pycurl.WRITEHEADER, indexfile)    # 将返回的HTTP HEADER定向到indexfile文件对象
c.setopt(pycurl.WRITEDATA, indexfile)    # 将返回的HTML内容定向到indexfile文件对象

try:
    c.perform()    # 提交请求
except Exception, e:
    print "connection error:"+str(e)
    indexfile.close()
    c.close()
    sys.exit()

NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)    # 获取DNS解析时间
CONNECT_TIME = c.getinfo(c.CONNECT_TIME)    # 获取连接时间
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)    # 获取从建立连接到传输所消耗的时间
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)    # 获取从建立连接到传输开始消耗的时间

TOTAL_TIME = c.getinfo(c.TOTAL_TIME)    # 获取传输的总时间
HTTP_CODE = c.getinfo(c.HTTP_CODE)    # 获取HTTP状态码
SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)    # 获取下载数据包大小
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)    # 获取HTTP头部大小
SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)    # 获取平均下载速度

print "HTTP状态码: %s" % (HTTP_CODE)
print "DNS解析时间: %.2f ms" % (NAMELOOKUP_TIME * 1000)
print "建立连接时间: %.2f ms" % (CONNECT_TIME * 1000)
print "准备传输时间: %.2f ms" % (PRETRANSFER_TIME * 1000)
print "传输开始时间: %.2f ms" % (STARTTRANSFER_TIME * 1000)
print "传输结束总时间: %.2f ms" % (TOTAL_TIME * 1000)
print "下载数据包大小: %d bytes/s" % (SIZE_DOWNLOAD)
print "HTTP头部大小: %d byte" % (HEADER_SIZE)
print "平均下载速度: %d bytes/s" % (SPEED_DOWNLOAD)

# 关闭文件及Curl对象
indexfile.close()
c.close()
