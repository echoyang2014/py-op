#!/usr/bin/env python
#coding:utf-8

import pexpect
import sys
ip = ""    # 定义目录主机
user = "root"    # 定义目录主机用户
passwd = ""    # 目标主机密码
target_file = "/usr/local/nginx-1.6.2/logs/access.log"    # 目标主机要传输的文件

child = pexpect.spawn('/usr/bin/ssh', [user+'@'+ip])
child.expect('(?i)password')
child.sendline(passwd)
child.expect('#')
child.sendline('tar -zcf /data/logs/nginx_access.tar.gz '+target_file)
child.expect('#')
child.sendline('exit')

child = pexpect.spawn('/usr/bin/scp', [user+'@'+ip+':/data/logs/nginx_access.tar.gz', '/home'])
child.expect('(?i)password')
child.sendline(passwd)
child.expect(pexpect.EOF)    # 匹配缓冲区结尾，保证文件复制正常完成
