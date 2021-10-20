import requests
url = "http://nadocoding.tistory.com/"
header = {"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}

res = requests.get(url, headers=header)
res.raise_for_status()
with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)
