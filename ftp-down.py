#!/usr/bin/env python
#coding:utf-8

from __future__ import unicode_literals    # 使用unicode编码
import pexpect
import sys

child = pexpect.spawnu('ftp ftp.openbsd.org')
child.expect('(?i)name .*: ')    # (?i)表示后面的字符串正则匹配忽略大小写
child.sendline('anonymous')
child.expect('(?i)password')
child.sendline('pexpect@sourceforge.net')
child.expect('ftp> ')
child.sendline('bin')    # 启用二进制传输模式
child.expect('ftp> ')
child.sendline('get robots.txt')
child.expect('ftp> ')
sys.stdout.write(child.before)    # 输出匹配'ftp> '之前的输入与输出
print 'successfully received the file'
child.sendline('bye')
