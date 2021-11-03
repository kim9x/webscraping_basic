import re
import requests
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def print_news(index, title, link):
    print("{}. {}".format(index, title))
    print("    (링크: {})".format(link))

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%8B%A0%ED%9D%A52%EB%8F%99+%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=hU%2FCldprvxsssCeRw7sssssss2K-468148"
    soup = create_soup(url)

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
    print()

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3) # limit=3 => 3개까지만 찾아
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip() # == news.div.a.get_text().strip()
        link = url + news.find("a")["href"].strip()
        print_news(index+1, title, link)
    print()

def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)
    for index, news in enumerate(news_list):
        img = news.find("img")
        a_idx = 0 
        if img:
            a_idx = 1 # img 태그가 있으면 1번째 a태그의 정보를 사용

        title = news.find_all("a")[a_idx].get_text().strip()
        link = news.find("a")["href"]
        print_news(index+1, title, link)
    print()

def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]: # 8문장이 있다고 가정할 때, 5~8까지(index 기준 4~7 ) 잘라서 가져옴
        print(sentence.get_text().strip())
    print() 
    for sentence in sentences[:len(sentences)//2]: # 8문장이 있다고 가정할 때, 0~4까지(index 기준 1~3) 잘라서 가져옴
        print(sentence.get_text().strip())
    print("(한글 지문)")



    print()

if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_headline_news() # 헤드라인 뉴스 정보 가져오기
    scrape_it_news() # IT 뉴스 정보 가져오기
    scrape_english() # 오늘의 영어 회화 가져오기