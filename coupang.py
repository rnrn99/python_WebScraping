import requests
import re
from bs4 import BeautifulSoup

for i in range(1, 6):
  url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(i)
  headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
  res = requests.get(url, headers=headers)
  res.raise_for_status()
  soup = BeautifulSoup(res.text, "lxml")

  # 아이템 목록 가져오기

  items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
  # firstItem = items[0].find("div", attrs={"class":"name"}).get_text()
  # print(firstItem)

  # for item in items:
  #   name = item.find("div", attrs={"class":"name"}).get_text()
  #   price = item.find("strong", attrs={"class":"price-value"}).get_text()
  #   rate = item.find("em", attrs={"class":"rating"}).get_text()
    # print("제품명 : ", name)
    # print("가격 : ", price)
    # print("평점 : ", rate)
    # print("---------------------------------------------------------------------")
    

  # 상품 목록 조건 설정

  for item in items:
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
      # print("<<<<<광고 상품 제외>>>>>")
      continue

    name = item.find("div", attrs={"class":"name"}).get_text()
    if "Apple" in name:
      # print("<<<<<Apple 상품 제외>>>>>")
      continue

    price = item.find("strong", attrs={"class":"price-value"}).get_text()

    rate = item.find("em", attrs={"class":"rating"})
    if rate:
      rate = rate.get_text()
    else:
      # print("<<<<<평점 없는 상품 제외>>>>>")
      continue

    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})
    if rate_cnt:
      rate_cnt = rate_cnt.get_text()
      rate_cnt = rate_cnt[1: -1]
    else:
      continue

    link = "https://www.coupang.com" + item.find("a", attrs={"class":"search-product-link"})["href"]

    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
      print(f"제품명 : {name}")
      print(f"가격 : {price}",)
      print(f"평점 : {rate} ({rate_cnt})")
      print(f"구매링크 : {link}")
      print("-"*100)



