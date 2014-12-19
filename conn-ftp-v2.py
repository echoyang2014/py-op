#!/usr/bin/env python
#coding:utf-8

import pexpect

child = pexpect.spawn('ftp ftp.openbsd.org')    # 运行ftp命令
info = file('ftpinfo.txt', 'w')    # 记录连接日志信息
child.logfile = info
child.expect('Name .*: ')    
child.sendline('anonymous')    # 输入ftp账号信息
child.expect('Password')    # 匹配密码输入提示
child.sendline('pexpect@sourceforge.net')    # 输入ftp密码
# 调用interact()让出控制权，用户可以继续当前的会话手工控制子程序
child.interact()
child.close()
