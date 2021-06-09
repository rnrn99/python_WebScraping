# 동적 페이지 스크래핑 - 할인하는 영화만 가져오기(제목, 할인 전 가격, 할인 후 가격,링크)

import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

# headless 옵션 설정
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36")

url = "https://play.google.com/store/movies/top"
browser = webdriver.Chrome(options=options)
browser.get(url)

# 스크롤 내려서 영화 목록 불러오기
# browser.execute_script("window.scrollTo(0,1080)")

# 현재 문서 높이 가져오기
prevHeight = browser.execute_script("return document.body.scrollHeight")
interval = 1

while True:
    # 화면 제일 아래로 스크롤 내리기
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    time.sleep(interval)

    curHeight = browser.execute_script("return document.body.scrollHeight")

    if curHeight == prevHeight:
        break

    prevHeight = curHeight

# 스크린샷 찍기
browser.get_screenshot_as_file("google_movie.png")

soup = BeautifulSoup(browser.page_source, "lxml")

# 리스트 형태로 감싸면 [A, B] A에 해당하는 거랑 B에 해당하는 거 모두 가져옴
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
# print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    originalPrice = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    if originalPrice:
        originalPrice = originalPrice.get_text()
        print(f"제목 : {title}")
        print(f"{originalPrice} -> {price}")
        print(f"https://play.google.com{link}")
        print("-"*70)
    else:
        continue

browser.quit()