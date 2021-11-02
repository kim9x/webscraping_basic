# [출력 결과]
# ============ 매물 1 ============
# 거래: 매매
# 면적: 84/59 (공급/전용)
# 가격: 165,000 (만원)
# 동: 214동
# 층: 고/23
# ============ 매물 2 ============
# ...


import requests
from bs4 import BeautifulSoup
url = "https://realty.daum.net/home/apt/danjis/38487"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

with open("quiz.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())

houses = soup.find_all("div", attrs={"class":"css-1dbjc4n r-13awgt0 r-1mlwlqe r-eqz5dr"})
for house in houses:
    print(house.find("div", attrs={"class":"css-1563yu1"})).get_text()
print(len(houses))