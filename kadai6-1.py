import requests
import pandas as pd

APP_ID = "48d387d4f2f9ac67eb1eebfe1a92823c583f4804"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId":"0003191320",
    "lang": "J"  # 日本語を指定
}
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()

# # 統計データからデータ部取得
# values = data['GET_STATS_DATA']['STATISTICAL_DATA']['DATA_INF']['VALUE']
 
# # JSONからDataFrameを作成
# df = pd.DataFrame(values)

print(data)
