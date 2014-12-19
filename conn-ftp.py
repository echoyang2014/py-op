#!/usr/bin/env python
#coding:utf-8

from __future__ import unicode_literals    # 使用unicode编码
import pexpect
import sys

child = pexpect.spawnu('ftp ftp.openbsd.org')    # 运行ftp命令
info = file('ftp.txt', 'w')    # 记录连接日志信息
child.logfile = info
# 匹配账号输入提示，(?i)表示后面的字符串正则匹配忽略大小写
child.expect('(?i)name .*: ')    
child.sendline('anonymous')    # 输入ftp账号信息
child.expect('(?i)password')    # 匹配密码输入提示
child.sendline('pexpect@sourceforge.net')    # 输入ftp密码
# 调用interact()让出控制权，用户可以继续当前的会话手工控制子程序
child.interact()
child.sendline('bye')
child.close()
