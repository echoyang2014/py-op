#!/usr/bin/env python
#coding:utf-8

import paramiko

hostname = ''
username = ''
password = ''
paramiko.util.log_to_file('syslogin.log')    # 发送paramiko日志到syslogin.log文件
ssh = paramiko.SSHClient()    # 创建一个ssh客户端client对象
ssh.load_system_host_keys()    # 获取客户端host_keys,默认~/.ssh/know_hosts,非默认路径需指定
ssh.connect(hostname = hostname, username = username, password = password)
stdin, stdout, stderr = ssh.exec_command('free -m')
print stdout.read()
ssh.close()
