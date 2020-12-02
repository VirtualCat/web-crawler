import requests
import pprint as pp
url = 'https://netreg.isu.edu.tw/Wapp/wap_check.asp'

user = 'isu10603017a'
password = 'howard990523'

p = {
    'logon_id': user,
    'txtpasswd': password
}

with requests.session() as session:
    re_res = session.post(url, data = p, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
    })
    pp.pprint(re_res.text)
    print("OK")

