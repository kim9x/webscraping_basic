import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# print(res.text)

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0].find("div", attrs={"class":"name"}).get_text())
# print(items[0].find("strong", attrs={"class":"price-value"}).get_text())

for item in items:

    ad_badge = item.find("span", attrs={"class":"ad-badge-text"}) # 광고
    if ad_badge:
        print(" <광고 상품 제외합니다.>")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text() # 제품명

    # 애플 제품 제외
    if "Apple" in name:
        print(" <Apple 상품 제외합니다.>")
        continue

    # if "2020" in name:
    #     print(" <2020 상품 제외합니다.>")
    #     continue

    price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격

    # 리뷰 100개 이상, 평점 4.5 이상 된는 것만 조회
    rate = item.find("em", attrs={"class":"rating"}) # 평점
    if rate:
        rate = rate.get_text()
    else:
        print(" <평점 없는 상품 제외합니다.>")
        continue

    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) # 평점 수
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        # 음수 값은 맨 뒤쪽을 의미한다.
        rate_cnt = rate_cnt[1:-1]
        # print("리뷰 수:", rate_cnt)
    else:
        print(" <평점 수 없는 상품 제외합니다.")

    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        print(name, price, rate, rate_cnt)
    

