#문자열 내장 함수

a = "Hello, World."

# dir() 함수: 함수가 가지고 있는 속성과 메소드 목록을 반환하는 파이썬 내장 함수
print(dir(a)) # str 자료형이 제공하는 속성과 메소드
print(dir(7)) # int 자료형이 제공하는 속성과 메소드
print(dir([1,2,3])) # list 자료형이 제공하는 속성과 메소드

# len() 함수: 객체의 길이를 반환하는 파이썬 내장 함수
print(len(a))
print(len([7, 7, 7]))

# 대소문자를 변환해주는 문자열 메소드
print(a.upper()) #대문자로 변환
print(a.lower()) #소문자로 변환
print(a.capitalize()) #문자열의 첫 번째, 글자를 대문자로 변환
print(a.title()) #각 단어의 첫 번째, 글자를 대문자로 변환

# 문자열의 공백 문자나 or 특정 문자를 제거해주는 문자열 메소드

a = "\t Python \n"
print("[" + a + "]")
print("[" + a.lstrip() + "]") #외쪽 공백 문자 제거
print("[" + a.rstrip() + "]") #오른쪽 공백 문자 제거
print("[" + a.strip() + "]") #양쪽 공백 문자 제거

a = "***Python***"
print(a.lstrip("*")) #왼쪽 특정문자 제거
print(a.rstrip("*")) #오른쪽 특정문자 제거
print(a.strip("*")) #특정문자 제거

s = "Hello, World. Welcome, Python!"

#부분 문자열이 처음 등장하는 위치(인덱스)를 알려주는 메소드
print(s.find("Hello")) #인덱스 반환
print(s.index("Hello")) #인덱스 반환

print(s.find("Java")) #인덱스 반환, -1
#print(s.index("Java")) #인덱스 반환, 에러 발생

#부분 문자열이 몇 번 나오는지 알려주는 문자열 메소드
print(s.count("Hello")) #등장 횟수

#문자열 포함 여부를 알려주는 연산자
print("Python" in s) #포함(True)
print("Java" in s) #미포함(False)
print("Java" not in s) # 반대로
#특정 preffix로 시작하고 있는지를 알려주는 연산자
print(s.startswith("Hello")) #True

#특정 preffix로 끝나는지를 알려주는 연산자
print(s.endswith("Python!")) #True

#이전 문자열을 새로운 문자열로 치환하는 문자열 메소드
#.replace는 새문자열을 만듦
print(s.replace("Python", "Programming")) #전체 치환
print(s.replace("Python", "Programming", 1)) #1개만 치환

#판별 문자열 메소드
print("123".isdigit()) #숫자면 True
print("ⅠⅣⅦⅩⅡⅤⅧⅪⅢⅨⅫⅥ".isnumeric()) #숫자면, 한자, 로마 포함 True
print("abc".isalpha()) #알파벳이면
print("a1b2c3".isalnum()) #알파벳 + 숫자면 
print("\t \n".isspace()) #공백 문자면
print("TRUE".isupper()) #대문자인지
print("true".islower()) #소문자인지
#구분자를 기준으로 문자열을 분리하는 문자열 메소드
a = "apple, banana, kiwi"
fruits = a.split(", ") #", "를 기준으로 분리(기본값 공백)
print(fruits) #리스트가 만들어짐

# Iterable(반복가능) 객체안의 문자열을 결합하는 문자열 메소드
print(", ".join(fruits)) #","로 구분