import requests

res = requests.get("https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo")
res.raise_for_status()

with open("kbo.html", "w", encoding="utf8") as f:
    f.write(res.text)