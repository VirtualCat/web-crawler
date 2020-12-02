import urllib.request as req
import bs4

url = 'https://netreg.isu.edu.tw/Wapp/Wap_indexmain2.asp'

# 建立 Request 物件，附加 headers 資訊
request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

#print(data)

root = bs4.BeautifulSoup(data, "html.parser")

n = root.find_all("span", style="font-size:20px;")

for m in n:
    if m.a == None:
        print(m.string)