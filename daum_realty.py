from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# headless 옵션 설정
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36")

# 다음 페이지 > 검색창에 입력 > enter
url = "https://www.daum.net/"
browser = webdriver.Chrome(options=options)
browser.get(url)

browser.find_element_by_class_name("tf_keyword").send_keys("송파 헬리오시티"+Keys.ENTER)

# 매물 표 가져오기
soup = BeautifulSoup(browser.page_source, "lxml")

rows = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")

# for i, row in enumerate(rows):
#     transaction = row.find("td", attrs={"class":"col1"}).get_text()
#     area = row.find("td", attrs={"class":"col2"}).get_text()
#     price = row.find("td", attrs={"class":"col3"}).get_text()
#     address = row.find("td", attrs={"class":"col4"}).get_text()
#     floor = row.find("td", attrs={"class":"col5"}).get_text()

#     print("="*10, "매물 {}".format(i + 1), "="*10)
#     print(f"거래 : {transaction}")
#     print(f"면적 : {area} (공급/전용)")
#     print(f"가격 : {price} (만원)")
#     print(f"동 : {address}")
#     print(f"층 : {floor}")

for i, row in enumerate(rows):
    col = row.find_all("td")

    print("="*10, "매물 {}".format(i + 1), "="*10)
    print("거래 :", col[0].get_text().strip())
    print("면적 :", col[1].get_text().strip() ,"(공급/전용)")
    print("가격 :", col[2].get_text().strip() ,"(만원)")
    print("동 :",col[3].get_text().strip())
    print("층 :",col[4].get_text().strip())

browser.quit()

