from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("http://naver.com")

enterPage = browser.find_element_by_class_name("link_login")
enterPage.click()

browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("naver_pw")

loginBtn = browser.find_element_by_id("log.login")
loginBtn.click()

# 로그인 시 자동입력방지문자 뜸 그래도 제대로 동작함
# 참조하기 : https://jaeseokim.github.io/Python/python-Selenium을-이용한-웹-크롤링-Naver-login-후-구독-Feed-크롤링/