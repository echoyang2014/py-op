#!/usr/bin/env python
#coding:utf-8

# pip install dnspython

# A记录：将主机名转换成IP地址

import dns.resolver

domain = raw_input("Please input an domain: ")    # 输入域名地址

A = dns.resolver.query(domain, 'A')    # 指定查询类型为A记录
for i in A.response.answer:    # 通过response.answer方法获取查询回应信息
    for j in i.items:    # 遍历回应信息
        print j.address
