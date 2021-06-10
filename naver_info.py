import re
import requests
from bs4 import BeautifulSoup


def createSoup(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def weather():
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8'
    soup = createSoup(url)

    cast = soup.find("p", attrs={"class": "cast_txt"}).get_text()

    curTemp = soup.find("p", attrs={"class": "info_temperature"}).get_text().replace("도씨", "")
    minTemp = soup.find("span", attrs={"class": "min"}).get_text()
    maxTemp = soup.find("span", attrs={"class": "max"}).get_text()

    dayRainRate = soup.find("span", attrs={"class": "point_time morning"}).get_text().strip()
    nightRainRate = soup.find("span", attrs={"class": "point_time afternoon"}).get_text().strip()

    airInfo = soup.find("dl", attrs={"class": "indicator"})
    dust = airInfo.find_all("dd")[0].get_text()
    ultrafineDust = airInfo.find_all("dd")[1].get_text()

    print("[ 오늘의 날씨 ]")
    print(cast)
    print(f"현재 {curTemp} (최저 {minTemp} / 최고 {maxTemp})")
    print(f"오전 {dayRainRate} / 오후 {nightRainRate}")
    print(f"미세먼지 {dust}")
    print(f"초미세먼지 {ultrafineDust}")
    print()


def headlineNews():
    url = 'https://news.naver.com'
    soup = createSoup(url)

    newsList = soup.find("ul", attrs={"class": "hdline_article_list"}).find_all("li", limit=3)

    print("[ 헤드라인 뉴스 ]")
    for i, news in enumerate(newsList):
       title = news.find("a").get_text().strip()
       link = url + news.find("a")["href"]
       print(f"{i + 1}. {title}")
       print(f" (링크 : {link})")
    print()

def itNews():
    url = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230'
    soup = createSoup(url)

    newsList = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)

    print("[ IT 뉴스 ]")
    for i , news in enumerate(newsList):
        index = 0
        img = news.find("img")

        if img:
            index = 1
        title = news.find_all("a")[index].get_text().strip()
        link = news.find_all("a")[index]["href"]
        print(f"{i + 1}. {title}")
        print(f" (링크 : {link})")
    print()

def english():
    url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english'
    soup = createSoup(url)

    print("[ 오늘의 영어회화 ]")

    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})

    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())
    
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())
   

if __name__ == '__main__':
    weather()
    headlineNews()
    itNews()
    english()
