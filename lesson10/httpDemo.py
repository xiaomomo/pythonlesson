import requests

headers = {'Authorization': 'APPCODE 2c571bbe36b24e9aa3cadaaee4d0adbf'}

r = requests.get(
    'https://saweather.market.alicloudapi.com/spot-to-weather?area=杭州&need3HourForcast=0&needAlarm=0&needHourData=0&needIndex=0&needMoreDay=0',
    headers=headers)

print(r.json()['showapi_res_body']['now']['weather'])
