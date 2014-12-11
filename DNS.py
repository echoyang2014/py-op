#!/usr/bin/env python
#coding:utf-8

# pip install dnspython

# A记录：用来指定主机名或域名的IP地址
# MX记录：邮件交换记录，定义邮件服务器的域名
# NS记录：标记区域的域名服务器及授权子域，用来指定该域名由哪个DNS服务器来解析
# CNAME记录：将一个域名指向另一个域名，再由另一个域名提供IP地址 
# PTR记录：反向解析，与A记录相反，用来指定IP地址的主机名或域名

import dns.resolver

domain = raw_input("Please input an domain: ")    # 输入域名地址

print '-' * 20
print "address records: "
A = dns.resolver.query(domain, 'A')   # 指定查询类型为A记录
for i in A.response.answer:   # 通过response.answer方法获取查询回应信息
    for j in i.items:    # 遍历回应信息
        if j.rdtype == 1:    # 避免 "AttributeError: 'CNAME' object has no attribute 'address'" 错误
            print j.address
        else:
            pass


print '-' * 20
print 'canonical name record: '
try:
    CNAME = dns.resolver.query(domain, 'CNAME')    # 指定查询类型为CNAME记录
    for i in CNAME.response.answer:    # 结果将回应CNAME后的目标域名
        for j in i.items:
            print j.to_text()
except:
    print "no canonical name record"


if domain.startswith('www.'):
    domain = domain[4:]
else:
    pass

print '-' * 20
print "name server records: "
NS = dns.resolver.query(domain, 'NS')    # 指定查询类型为NS记录
for i in NS.response.answer:
    for j in i.items:
        print j.to_text()

print '-' * 20
print "mail exchanger recods: "
MX = dns.resolver.query(domain, 'MX')    # 指定查询类型为MX记录
for i in MX:    # 遍历回应结果，输出MX记录的prefernce及exchanger信息
    print 'MX preference = {0}, mail exchanger = {1}'.format(
        i.preference, i.exchange)

