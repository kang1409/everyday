import smtplib
import requests
import datetime
# 负责构造文本
from email.mime.text import MIMEText
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header


#获取天气信息
r = requests.get('http://t.weather.sojson.com/api/weather/city/101110101')
r.encoding = 'utf-8'
a = r.json()
type = a["data"]["forecast"][0]["type"]         #天气
city = a["cityInfo"]["city"]                    #城市
temp_high = a["data"]["forecast"][0]["high"]    #最高温
temp_low = a["data"]["forecast"][0]["low"]      #最低温
time = a["time"] + a["data"]["forecast"][0]["week"]



# SMTP服务器,这里使用163邮箱
mail_host = "smtp.163.com"
# 发件人邮箱
mail_sender = "13028577808@163.com"
# 邮箱授权码,注意这里不是邮箱密码,如何获取邮箱授权码,请看本文最后教程
mail_license = "PROMXAGTFIVOGYQB"
# 收件人邮箱，可以为多个收件人
mail_receivers = ["2754523470@qq.com", "3519192336@qq.com"]

#, "3519192336@qq.com", "2985496686@qq.com"

mm = MIMEMultipart('related')

# 邮件主题
subject_content = """每日天气定时邮件！！！"""
# 设置发送者,注意严格遵守格式,里面邮箱为发件人邮箱
mm["From"] = "sender_name<13028577808@163.com>"
# 设置接受者,注意严格遵守格式,里面邮箱为接受者邮箱
mm["To"] = "receiver_1_name<******@qq.com>,receiver_2_name<******@outlook.com>"
# 设置邮件主题
mm["Subject"] = Header(subject_content, 'utf-8')

#获取时间计算时间差
starttime = datetime.datetime.now()
endtime = datetime.datetime.strptime("2021-06-11", "%Y-%m-%d")
time = starttime - endtime

# 邮件正文内容
body_content = """
宝贝早上好呀!
嘿嘿嘿，今日天气状况奉上：💕💕💕😁
今日时间： %s   
今天是我们在一起的第%s天
城市：%s
天气：%s
最高温：%s    最低温：%s 
"""%(starttime, time, city, type, temp_high, temp_low)
# 构造文本,参数1：正文内容，参数2：文本格式，参数3：编码方式
message_text = MIMEText(body_content,"plain","utf-8")
# 向MIMEMultipart对象中添加文本对象
mm.attach(message_text)

#微信推送
msg = body_content
token = 'd72887890d5c4164b34d6d1dfaaba92e'  # 前边复制到那个token
token_1 = "e667729511074a79ac582a07c65fe2fc"
title = '每日天气定时邮件！！！'
content = msg
template = 'html'
url = f"https://www.pushplus.plus/send?token={token}&title={title}&content={content}&template={template}"
url_1 = f"https://www.pushplus.plus/send?token={token_1}&title={title}&content={content}&template={template}"
print(url)
print(url_1)
r = requests.get(url=url)
r_1 = requests.get(url=url_1)
print(r.text)
print(r_1.text)



# 创建SMTP对象
stp = smtplib.SMTP()
# 设置发件人邮箱的域名和端口，端口地址为25
stp.connect(mail_host, 25)
# set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
stp.set_debuglevel(1)
# 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
stp.login(mail_sender,mail_license)
# 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
stp.sendmail(mail_sender, mail_receivers, mm.as_string())
print("邮件发送成功")
# 关闭SMTP对象
stp.quit()
