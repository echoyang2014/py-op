#!/usr/bin/env python
#coding:utf-8

import paramiko
username = ''
password = ''
hostname = ''
port = 22

try:
    t = paramiko.Transport((hostname, port))
    t.connect(username = username, password = password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put("/home/test/info.db", "/data/test/info.db")
    sftp.get("/data/test/info_1.db", "/home/test/info_1.db")
    sftp.mkdir("/home/testdir", 0755)
#   sftp.rmdir("/home/testdir")
    sftp.rename("/home/test.sh", "/home/testfile.sh")
    print sftp.stat("/home/testfile.sh")
    print sftp.listdir("/home")
    t.close
except Exception, e:
    print str(e)

