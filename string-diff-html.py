#!/usr/bin/env python
#coding:utf-8
import difflib

text1 = """text1：
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
"""

text1_lines = text1.splitlines()    # 以行进行分隔，以便进行对比  

text2 = """text2:
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5"""

text2_lines = text2.splitlines()

d = difflib.HtmlDiff()    # 创建Differ()对象
print d.make_file(text1_lines, text2_lines)


"""比较结果符号含义说明：
'-'  包含在第一个序列行中，但不包含在第二个序列行
'+'  包含在第二个序列行中，但不包含在第一个序列行
' '  两个序列行一致
'?'  标志两个序列行存在增量差异
'^'  标志出两个序列存在的差异字符"""
