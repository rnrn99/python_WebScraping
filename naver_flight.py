from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://flight.naver.com/flights/")

browser.find_element_by_link_text("가는날 선택").click()

# 이번 달 27, 28일
browser.find_elements_by_link_text("27")[0].click()
browser.find_elements_by_link_text("28")[0].click()

# 다음 달 27, 28일
# browser.find_elements_by_link_text("27")[1].click()
# browser.find_elements_by_link_text("28")[1].click()

# 제주도 선택
browser.find_element_by_link_text("도착").click()
browser.find_element_by_xpath("//*[@id='l_1']/div/div[2]/div[2]/table[1]/tbody/tr[1]/td[1]/a").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# 로딩 기다려서 결과 출력하기
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    print(elem.text)
finally:
    browser.quit()
