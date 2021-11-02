from typing import cast
import requests
from bs4 import BeautifulSoup

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%8B%A0%ED%9D%A52%EB%8F%99+%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=hU%2FCldprvxsssCeRw7sssssss2K-468148"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    casts = soup.find("p", attrs={"class":"summary"})
    weather = casts.find("span", attrs={"class":"weather before_slash"}).get_text()
    cast = casts.get_text().replace("맑음", "").strip()
    # print(weather)


    curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().strip()
    # print(curr_temp)
    max_temp = soup.find("span", attrs={"class":"highest"}).get_text() # 최고 온도
    min_temp = soup.find("span", attrs={"class":"lowest"}).get_text() # 최저 온도
    # print(max_temp)
    # print(min_temp)

    rain_rate = soup.find("div", attrs={"class":"cell_weather"}) # 강수 확률
    morning_rain_rate = rain_rate.find_all("span", attrs={"class":"rainfall"})[0].get_text()
    afternoon_rain_rate = rain_rate.find_all("span", attrs={"class":"rainfall"})[1].get_text()
    # print(rain_rate)
    # print(morning_rain_rate)
    # print(afternoon_rain_rate)
    dust = soup.find("ul", attrs={"class":"today_chart_list"})
    # print(dust)
    pm10 = dust.find_all("li")[0].get_text().strip() # 미세먼지
    pm25 = dust.find_all("li")[1].get_text().strip() # 초미세먼지
    # print(pm10)
    # print(pm25)
    
    print(f"{weather}, {cast}")
    print("{} ({} / {})".format(curr_temp, min_temp, max_temp))
    print("오전 강수 확률 {} / 오후 강수 확률 {}".format(morning_rain_rate, afternoon_rain_rate))
    print()
    print(pm10)
    print(pm25)
    print

if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨 정보 가져오기