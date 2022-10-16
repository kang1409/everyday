import requests

msg = """测试一下下"""
token = 'd72887890d5c4164b34d6d1dfaaba92e'  # 前边复制到那个token
token_1 = "d4e066c052e24183b991d3bbc6799d72"
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


