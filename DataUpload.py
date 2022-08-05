import requests, json

def SensorUpload(trapID, workDate, temp, humid, Direc, Speed, rainfall):
    data = {
    "trapId": str(trapID),
    "workDate": str(workDate),
    "temperature": str(temp),
    "humidity": str(humid),
    "windDirection": str(Direc),
    "windSpeed": str(Speed),
    "rainfall": str(rainfall)
    }

    URL = 'http://digitalfarm.kr/api/trap/sensor'
    headers = {'Content-Type': 'application/json; charset=utf-8'}

    res = requests.post(URL, data=json.dumps(data), headers=headers)

    print(res.text)

#SensorUpload(1, 20220214181805, 10, 5, 'N', 15, 10)