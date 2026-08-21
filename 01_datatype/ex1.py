# 변수
# 파이썬은 동적 타이핑 언어
a = 2
b = 3
print(a, b) # 2 3
print(a)
print(b) # 파이썬은 기본적으로 다른 줄에 적는다.
print(a, end = " 마이야히 ") #end = ""를 통해, 줄바꿈 대신 공백으로 구분할 수 있다.
print(b)
print(a, b, sep = ", ") #sep = ""을 통해 원하는 문자로 구분할 수 있다.

# a = 2, b = 3는 a = (2, b) = 3와 같다.
a = 2, b
print(a, type(a))

a = 2; b = 3 # 세미콜론을 통해 한 줄에서도 구분
print(a, b, sep = "") # 23

x = y = z = 0
a, b = 2, 3 # a와 b 각각에 각각의 값을 대입함, 튜플 언팩킹
print(a, b, sep = ", ") # 2, 3

# 값 swap
temp = a
a = b
b = temp
print(a, b, sep = ", ") # 3, 2

# 값 swap, 튜플 언팩킹 방식 활용
a, b = b, a
print(a, b, sep = ", ") # 2, 3

# 변수명 규칙 (C와 동일)
# 1. 문자, 숫자, 언더바만 가능
# 2. 숫자로 시작 불가
# 3. 대소문자 구분 가능
# 예약어는 사용 불가
name2 = "qwrgdcx"
#2name = "qwrgdcx", 숫자로 시작하는 건 불가능하다.
_name = "qwrgdcx" # 언더바로 시작하는 건 가능하다.
#class = "qwrgdcx", 예약어는 변수명으로 활용할 수 없다.
#name! = "qwrgdcx", 특수문자는 언더바만
이름 = "qwrgdcx" # 한글로 가능하나 영어 추천
print(name2, _name, 이름, sep = ", ")

student_name = "qwrgdcx" #스네이크 케이스
studentName = "qwrgdcx" #캐믈 케이스
print(student_name, studentName, sep = ", ")
MAX_COUNT = 100 #상수는 대문자로 표현
print(MAX_COUNT)