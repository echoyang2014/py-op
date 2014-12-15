#!/usr/bin/env python
#coding:utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

HOST = "smtp.126.com"
SUBJECT = u"官网业务服务质量周报"
TO = "to@qq.com"
FROM = "from@126.com"

def addimg(src, imgid):
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', imgid)
    return msgImage

msg = MIMEMultipart('related')

msgtext = MIMEText("<font color=red>官网业务周平均延时图表:<br><img src=\"cid:weekly\" border=\"1\"><br>详细内容见附件。</font>","html","utf-8")
msg.attach(msgtext)
msg.attach(addimg("img/weekly.png", "weekly"))

# 创建一个MIMEText对象，附加week_report.xlsx文档
attach = MIMEText(open("doc/week_report.xlsx", "rb").read(), "base64", "utf-8")
attach["Content-Type"] = "application/octet-stream"    # 指定文件格式类型
# 指定Content-Disposition值为attachment则出现下载保存对话框，保存的默认文件名使用filename指定
# 由于qqmail使用gb18030页面编码，为保证中文文件名不出现乱码，对文件名进行编码转换
attach["Content-Disposition"] = "attachment; filename=\"业务服务质量周报(12周).xlsx\"".decode("utf-8").encode("gb18030")
msg.attach(attach)

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
