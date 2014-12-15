#!/usr/bin/env python
#coding:utf-8

# 通过MIMEText类来实现HTML格式的邮件，当要求包含图片数据的邮件内容时，需要引用MIMEImage类
# 若邮件主体由多个MIME对象组成，则同时需引用MIMEMultipart类来进行组装

import smtplib
from email.mime.multipart import MIMEMultipart    # 导入MIMEMultipart类
from email.mime.text import MIMEText    # 导入MIMEText类
from email.mime.image import MIMEImage    # 导入MIMEImage类

HOST = "smtp.126.com"
SUBJECT = u"业务性能数据报表"
TO = "to@qq.com"
FROM = "from@126.com"

def addimg(src, imgid):    # 添加图片函数，参数1：图片路径，参数2：图片id
    fp = open(src, 'rb')    # 打开文件
    msgImage = MIMEImage(fp.read())    # 创建MIMEImage对象，读取图片内容并作为参数
    fp.close()    # 关闭文件
    msgImage.add_header('Content-ID', imgid)    # 指定图片文件的Content-ID，imgid，<img>标签中的src用到
    return msgImage    # 返回msgImage对象

msg = MIMEMultipart('related')    # 创建MIMEMultipart对象，采用related定义内嵌资源的邮件体

# 创建一个MIMEText对象，HTML元素包括表格<table>及图片<img>
msgtext = MIMEText("""    
        <table width="600" border="0" cellspacing="0" cellpadding="4">
            <tr bgcolor="#CECFAD" height="20" style="font-size:14px">
                <td colspan=2>*官网性能数据  <a href="monitor.domain.com">更多>></a></td>
            </tr>
            <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
                <td>
                    <img src="cid:io"></td><td>
                    <img src="cid:key_hit"></td>
            </tr>
            <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
                <td>
                    <img src="cid:men"></td><td>
                    <img src="cid:swap"></td>
            </tr>
        </table>""","html","utf-8")    # <img>标签的src属性是通过Content-ID来引用的

msg.attach(msgtext)    # MIMEMultipart对象附加MIMEText的内容

# 使用MIMEMultipart对象附加MIMEImage的内容
msg.attach(addimg("img/bytes_io.png","io"))    
msg.attach(addimg("img/myisam_key_hit.png","key_hit"))
msg.attach(addimg("img/os_mem.png","men"))
msg.attach(addimg("img/os_swap.png","swap"))

msg['Subject'] = SUBJECT
msg['From'] = FROM
msg['To'] = TO
try:
    server = smtplib.SMTP(HOST, "25")
    server.starttls()
    server.login("from@126.com", "passwd")
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
    print "邮件发送成功！"
except Exception, e:
    print "失败: "+str(e)

