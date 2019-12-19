from urllib import request

import chardet

response = request.urlopen("https://bj.lianjia.com/")
html = response.read()
# 获取读入的 html 的编码，不用写死了
charset = chardet.detect(html)
print(charset)
html = html.decode(charset.get("encoding"))
print(html)
