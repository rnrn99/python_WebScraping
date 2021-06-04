# selenium practice
# 시작하기 전 > selenium 설치 > pip install selenium
#            > web driver 설치 > chrome version 확인 > chrome://version > 해당 version에 맞는 driver 설치

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("http://naver.com")

elem = browser.find_element_by_id("query")
elem.send_keys("셀레니움")
elem.send_keys(Keys.ENTER)

# 현재 탭만 닫기
browser.close()

# 모든 탭 닫기
browser.quit()