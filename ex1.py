# 1 연산자
# 산술 연산자
a = 10
b = 3

print(a + b) #13
print(a - b) #7
print(a * b) #30
print(a / b) #3.3333333333333335
print(a % b) #1

print(a // b) #몫을 구하는 연산자, 3
print(a ** b) #거듭제곱, 1000

# 복합대입 연산자
a += 4
print(a) #14

a -= 4
print(a) #10

#증감 연산자
# b = a++ 적용되지 않음
# b = ++a "
a += 1

#비교 연산자
print(3 == 3.0) #True, 파이썬은 값만 비교한다.
print("apple" < "apble") #False, 문자열의 크기는 사전순을 기준으로 한다.
print(1 < 2 < 3) #True, 1 < 2 && 2 < 3
print(1 < 2 and 2 < 3)
print(1 < 3 < 2) #False

#논리 연산자 (and, or, not)
print(True and True) #True
print(True or False) #True
print(not True) #False

# Short-circuit 테스트
a = 10
b = 0
#print(a / b) 에러가 발생한다, 0으로 나눌 수는 없음

if a > 0 or a / 0:
    print("yes") #yes, or 연산의 경우 앞만 보고 True일 경우 뒤에는 연산하지 않는다.
else:
    print("no")


