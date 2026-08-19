# 입출력 처리

a = input() #반드시 string으로 리턴
print(a) 
print(type(a)) #변수의 타입을 출력

#정수로 변환
a = input()
a = int(a) # 정수 타입으로 변환 
print(a, type(a))

a = int(input()) #위 두줄과 같다 -> 더 효율적
print(a, type(a))

# 실수 입력
a = float(input())
print(a, type(a))

#정수 2개 입력
#100
#200
a = int(input()) #100
b = int(input()) #200
print(a, b)

#100 200 #이렇게 입력하면, 에러남.
a = input().split() #띄어쓰기로 구분하고 싶을 경우 .split()함수를 통해, 원하는 문자로 구분
print(a, type(a))
#b = a[0] #실험용
#c = a[1] #실험용2
#print(b, c) #실험용3

#map(함수, 리스트)
a, b, c = map(int, input().split())
print(a, b, c) #변수 개수와 입력 개수가 일치 시, 이를 각각 배분
print(type(a))

#리스트 변환
a = list(map(int, input().split()))
print(a, type(a))


# made by qwrgdcx

