# 문자열
# "", '' 단, 쌍따음표를 권장한다.

a = "python"
print(a, type(a), sep = ", ") #python, <class 'str'>
b = 'python'
print(b, type(b), sep = ", ") #python, <class 'str'>
print(a == b) #True

# I'll be back
print("I'll be back") #I'll be back
print('I\'ll be back') # \: escape 문자 # I'll be back

multiline = """
Life is short
You need Python
""" # 여러줄 문자열을 쓸 때: 쌍따음표 혹은 홑따음표 3개를 연달아 작성하기
print(multiline)
def func():
    """이 함수는 테스트용입니다.""" # 함수에 대한 주석으로 사용 가능
    pass

print(func.__doc__) #함수에 적혀 있는 멀티라인 스트링을 출력, docstring: 멀티라인으로 첫! 번쨰 줄에 작성해야 함

# 문자열 연결
print("Hello, " + "Python") #Hello, Python
a = "Hello"
b = "world"
print(a, b, sep = ", ")

#문자열 반복
print("Hello, world" * 10) # Hello, world를 10번 출력
print((a + b) * 10) #Helloworld를 10번 출력

# print("Hello" + 10) #신택스 에러, 문자열과 숫자형은 함께 더할 수 없다. 같은 문자형 끼리만 가능

print("10" + "2") #102
print(int("10") + int("2")) #12

# 문장열 포매팅 (f-string)
name = "pororo"
age = 23

print(f"이름: {name}, 나이: {age}세") #이름: pororo, 나이: 23세
print(f"내년 나이: {age + 1}세") #내년 나이: 24세
print(f"{name.upper()}") #PORORO

pi = 3.141592

print(f"{pi:.3f}") #3.142
print(f"{pi:.3}") #3.14

num = 123456789

print(f"{num:,}") #123,456,789

print(f"{num:15d}") #      123456789
print(f"{num:<15d}") #123456789
print(f"{num:15}") #      123456789
print(f"{num:15,d}") #    123,456,789
print(f"{num:015,d}") #000,123,456,789
#test