#/usr/bin/env python
#coding:utf-8

# pip install IPy

from IPy import IP

ip_s = raw_input('Please input an IP or net-range: ')    # 接收用户输入，参数为IP地址或网段地址
ips = IP(ip_s)
if len(ips) > 1:    # 为一个网络地址
    print 'net: {0}'.format(ips.net())   # 输出网络地址
    print 'netmask: {0}'.format(ips.netmask())    # 输出网络掩码地址
    print 'broadcast: {0}'.format(ips.broadcast())    # 输出网络广播地址
    print 'reverse address: {0}'.format(ips.reverseNames()[0])    # 输出地址反向解析
    print 'subnet: {0}'.format(len(ips))    # 输出网络子网数
else:    # 为单个IP地址
    print 'reverse address: {0}'.format(ips.reverseNames()[0])    # 输出IP反向解析

print 'hexadecimal: {0}'.format(ips.strHex())    # 输出十六进制地址
print 'binary ip: {0}'.format(ips.strBin())    # 输出二进制地址
print 'iptype: {0}'.format(ips.iptype())    #输出地址类型，如PRIVATE, PUBLIC, LOOKBACK等
