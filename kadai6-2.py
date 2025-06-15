import requests

# URL設定
url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"

# 天気情報の取得
response = requests.get(url)

data = response.json()
print(data)

