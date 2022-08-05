import requests

def ImageUpload(trapId, workDate, Filename):
  url = "http://digitalfarm.kr/api/trap/upload/image"

  payload={
  'trapId': str(trapId),
  'workDate': str(workDate)
  }

  files=[
    ('uploadFile', (str(Filename),open('/home/test/Desktop/pictures/' +str(Filename),'rb'),'image/png'))
  ]
  headers = {}

  response = requests.request("POST", url, headers=headers, data=payload, files=files)

  print(response.text)

#ImageUpload(1, 20220214181305, '2022-01-26-01')