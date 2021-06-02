#정규식
import re

p = re.compile("ca.e")

# . (ca.e) : 하나의 문자를 의미 > care, cafe, case | caffe
# ^ (^de)  : 문자열의 시작을 의미 > desk, destiny | fade
# $ (se$)  : 문자열의 끝을 의미 > case, base | face

def print_match(text):
    if text:
        print("string : ", text.string)     # 입력받은 문자열 반환
        print("group : ", text.group())     # 일치하는 문자열 반환
        print("start : ", text.start())     # 일치하는 문자열의 시작 index 반환
        print("end : ", text.end())         # 일치하는 문자열의 끝 index 반환
        print("span : ", text.span())       # 일치하는 문자열의 시작과 끝 index 반환
        print("----------------------")
    else:
        print("매칭되지 않음")

# m = p.match("case")
m = p.match("careless")
print_match(m)

# match : 주어진 문자열의 처음부터 일치하는지 확인 > careless 입력 시 결과가 care로 매칭됨.

s = p.search("good care")
print_match(s)

# search : 주어진 문자열 중에 일치하는 게 있는지 확인 > good care 입력 시 결과가 care로 매칭됨.

lst = p.findall("careless cafe")
print(lst)

# findall : 일치하는 모든 것을 리스트 형태로 반환 > careless 입력 시 ['care'] 반환.

# 참조: https://www.w3schools.com/python/python_regex.asp