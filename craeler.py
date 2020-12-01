import urllib.request as req

url = 'https://netreg.isu.edu.tw/Wapp/Wap_indexmain2.asp'

# 建立 Request 物件，附加 headers 資訊
request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

print(data)