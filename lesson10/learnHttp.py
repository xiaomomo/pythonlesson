import requests

# 完整文档参照：http://docs.python-requests.org/zh_CN/latest/

# 1.默认
r = requests.get('https://api.github.com/events')
print(r)
# 2.带参数
requests.post('http://baidu.com', data = {'key':'value'})

# 3.其他HTTP方法
# requests.put('http://httpbin.org/put', data = {'key':'value'})
# requests.delete('http://httpbin.org/delete')
# requests.head('http://httpbin.org/get')
# requests.options('http://httpbin.org/get')

# 4. url后缀参数
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://baidu.com", params=payload)
print(r.url)

# 5. 获取请求返回数据
r = requests.get('https://api.github.com/events')
print(r.text)

# 6. 返回结果json解码
r = requests.get('https://api.github.com/events')
print(r.json())

# 7. 设置Header
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print(r.json())

# 8. 提交post表单
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://baidu.com", data=payload)
print(r.text)

# 9. 查看http响应头
r.headers

# 10. cookie
# 获取cookie
r.cookies['example_cookie_name']

# 设置cookie
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)

# 设置超时（秒单位）
requests.get('http://github.com', timeout=3)



