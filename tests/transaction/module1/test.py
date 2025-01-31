import requests
headers = {
    'Authorization': 'Bearer YOUR_TOKEN'
}

response = requests.get('https://api.example.com/data', headers=headers)


# 打印响应内容
print(response.text)