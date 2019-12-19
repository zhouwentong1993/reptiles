import json
from urllib import parse
from urllib import request

# req = request.Request("http://fanyi.baidu.com/")
# response = request.urlopen(req)
# print("url:", response.geturl())
# print("info:", response.info())
# print("getCOde:", response.getcode())

req = request.Request("https://fanyi.baidu.com/v2transapi?from=en&to=zh")
form_data = {'from': 'en', 'to': 'zh', 'query': 'hello', 'transtype': 'realtime', 'simple_means_flag': 3,
             'sign': 54706.276099, 'token': 'a0a3bea3aa93580849013e150dbdd1ac'}
data = parse.urlencode(form_data).encode('utf-8')
response = request.urlopen("https://fanyi.baidu.com/v2transapi?from=en&to=zh", data)
print(response)
html = response.read().decode('utf-8')
translate_result = json.load(html)
print(translate_result)
