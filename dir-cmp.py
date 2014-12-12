#!/usr/bin/env python
#coding:utf-8

import filecmp

a = "dir1"    # 定义左目录
b = "dir2"    #定义右目录

dirobj = filecmp.dircmp(a, b, ['test.py'])    #目录比较，忽略test.py文件

# 输出对比结果数据报表
dirobj.report()    # report()，比较当前指定目录中的内容
dirobj.report_partial_closure()    # report_partial_closure()，比较当前指定目录及第一级目录中的内容
dirobj.report_full_closure()    # report_full_closure()，递归比较所有指定目录的内容
print "left_list:"+str(dirobj.left_list)    # left_list，左目录中的文件及目录列表
print "right_list:"+str(dirobj.right_list)    # right_list，右目录中的文件及目录列表
print "common:"+str(dirobj.common)    # common，两边目录共同存在的文件或目录
print "left_only:"+str(dirobj.left_only)    # 只在左目录中的文件或目录
print "right_only:"+str(dirobj.right_only)    # 只在右边目录中的文件或目录
print "common_dirs:"+str(dirobj.common_dirs)    # 两边目录都存在的子目录
print "common_files:"+str(dirobj.common_files)    # 两边目录都存在的子文件
print "common_funny:"+str(dirobj.common_funny)    # 两边目录都存在的子目录（不同目录类型或os.stat()记录的错误）
print "same_file:"+str(dirobj.same_files)     # 匹配相同的文件
print "diff_files:"+str(dirobj.diff_files)    # 不匹配的文件    
print "funny_files:"+str(dirobj.funny_files)    # 两边目录中都存在，但无法比较的文件
