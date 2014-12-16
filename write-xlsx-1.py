#!/usr/bin/env python
#coding:utf-8

import xlsxwriter

workbook = xlsxwriter.Workbook('demo1.xlsx')    # 创建一个Excel文件
worksheet = workbook.add_worksheet()    # 创建一个工作表对象

worksheet.set_column('A:A', 20)    # 设定第一列（A）宽度为20像素
bold = workbook.add_format({'bold': True})    # 定义一个加粗的格式对象

worksheet.write('A1', 'Hello')    # A1单元格写入'Hello'
worksheet.write('A2', 'World', bold)    # A2单元格写入'World'并引用加粗格式对象bold
worksheet.write('B2', u'中文测试', bold)    # B2单元格写入中文并引用加粗格式对象bold


worksheet.write(2, 0, 32)    # 用行列表示法写入数字'32'，单元格下标以0开始，'2, 0'等价于'A3'
worksheet.write(3, 0, 35.5)
worksheet.write(4, 0, '=SUM(A3:A4)')    # 求A3:A4的和，并将结果写入'4, 0'，即'A5'
worksheet.insert_image('B5', 'img/os_mem.png')    # 在'B5'插入图片
workbook.close()    
