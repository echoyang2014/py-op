#!/usr/bin/evn python
#coding:utf-8

from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user = 'root'
env.hosts = ['', '']
env.password = ''

@task
@runs_once
def tar_task():    # 本地打包任务函数，只限执行一次
    with lcd("/data/logs"):
        local("tar -zcf access.tar.gz access.log")
@task
def put_task():    # 上传文件任务函数
    run("mkdir -p /logs")
    with cd("/logs"):
        with settings(warn_only = True):
            result = put("/data/logs/access.tar.gz", "/logs/access.tar.gz")
        if result.failed and not confirm("put file faild, Continue[Y/N]?"):
            abort("Aborting file put task!")
@task
def check_task():    # 检验文件任务函数
    with settings(warn_only = True):
        lmd5 = local("md5sum /data/logs/access.tar.gz", capture = True).split(' ')[0]
        rmd5 = run("md5sum /logs/access.tar.gz").split(' ')[0]
    if lmd5 == rmd5:
        print "OK"
    else:
        print "ERROR"

@task
def go():
    tar_task()
    put_task()
    check_task()
