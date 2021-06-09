import requests
from bs4 import BeautifulSoup

# 한국의 구글무비 페이지로 들어가기 위해서 user agent와 language 설정 필요

url = "https://play.google.com/store/movies/top"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'Accept-Language': 'ko-KR,ko'
}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", {"class":"ImZGtf mpg5gc"})

for movie in movies:
    title = movie.find("div", attrs = {"class":"WsMG1c nnK0zc"}).get_text()
    print(title)