# 조건 
# 1. 오늘의 날씨 정보
# 2. 헤드라인 뉴스 
# 3. 오늘의 영어 회화 지문

import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# headless 옵션 설정
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36")

url = "https://www.naver.com/"
browser = webdriver.Chrome(options=options)
browser.get(url)

# 날씨 정보 가져오기
# 날씨 검색 > 정보 추출
def weather():
    browser.find_element_by_class_name("input_text").send_keys("날씨" + Keys.ENTER)
    soup = BeautifulSoup(browser.page_source, "lxml")

    area = soup.find("span", attrs={"class":"btn_select"}).get_text()
    weatherTemp = soup.find("span", attrs={"class":"todaytemp"}).get_text()
    weatherList = soup.find("ul", attrs={"class":"info_list"}).find_all("li")

    print(f"[ {area}의 날씨 ]")
    print(f"  현재 온도 : {weatherTemp}℃")
    for i in range(0,3):
        print(" ",weatherList[i].get_text().strip())
    print()


# 헤드라인 뉴스 가져오기
# 네이버 뉴스 페이지 접속 > 정보 추출
def headlineNews():
    url = "https://news.naver.com/"
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, "lxml")

    headlineList = soup.find("ul",attrs={"class":"hdline_article_list"}).find_all("li")

    print("[ 헤드라인 뉴스 ]")

    for i, row in enumerate(headlineList):
        title = row.find("div", attrs={"class":"hdline_article_tit"}).get_text().strip()
        link = "https://news.naver.com/" + row.find("a")["href"]
        
        print("{}. ".format(i + 1), title)
        print(f"(링크 : {link})")
        print()


# 영어회화 문장과 예시 가져오기
# 해커스 오늘의 영어회화
def english():
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;"
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, "lxml")

    print("[ 오늘의 영어회화 ]")
    print()

    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})

    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())
    
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())


weather()
headlineNews()
english()
browser.quit()
