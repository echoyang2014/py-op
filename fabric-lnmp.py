#!/usr/bin/env python
#coding:utf-8

from fabric.colors import *
from fabric.api import *

env.user = 'root'
env.roledefs = {    # 定义业务角色分组
        'webservers': ['192.168.1.21', '192.168.1.22'],
        'dbservers': ['192.168.1.23']
        }

env.passwords = {
        'root@192.168.1.21: 22': 'passwd',
        'root@192.168.1.22: 22': 'passwd',
        'root@192.168.1.23: 22': 'passwd'
        }

@roles('webservers')    # webtask任务函数引用webservers角色修饰符
def webtask():    # 部署nginx php php-fpm等环境
    print yellow("Install nginx php php-fpm...")
    with settings(warn_only = True):    # 当warn_only=True, 函数执行出错时, 仅提示出错信息, 而不中止函数, 默认为False
        run("yum -y install nginx")
        run("yum -y install php-fpm php-mysql php-mbstring php-xml php-mcrypt php-gd")
        run("chkconfig --levels 235 php-fpm on")
        run("chkconfig --levels 235 nginx on")

@roles('dbservers')    # dbtask任务函数引用dbservers角色修饰符
def dbtask():    # 部署MySQL环境
    print yellow("Install MySQL...")
    with settings(warn_only = True):
        run("yum -y install mysql mysql-server")
        run("chkconfig --levels 235 mysqld on")

@roles('webservers', 'dbservers')    # publictask任务函数同时引用两个角色修饰符
def publictask():    # 部署公共类环境, 如epel ntp等
    print yellow("Install epel ntp...")
    with settings(warn_only = True):
        run("rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm")
        run("yum -y install ntp")

def deploy():
    execute(publictask)
    execute(webtask)
    execute(dbtask)

