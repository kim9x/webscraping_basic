import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url)


# 가는 날 선택 클릭
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

# print(browser.find_elements_by_link_text("27"))
time.sleep(2)

# xpath 기준으로 element가 위치할 때까지 최대 10초까지 기다려준다.
# XPATH 뿐만이 아닌 ID, CLASS_NAME, LINK_TEXT 등 사용 가능.
try:
    elem = wait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div[11]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[5]/button")))
    # 성공했을 때 동작 수행
    print(elem.text)
finally:
    browser.quit()

# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[11]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[5]/td[2]/button").click()
# wait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/div[1]/div[11]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[6]/button"))).click()
# wait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[1]/div[11]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[6]/button"))).click()


