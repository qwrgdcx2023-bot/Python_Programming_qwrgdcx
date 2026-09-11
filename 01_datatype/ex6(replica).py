a = "Python"

# 문자열은 원본 불멸이다.

#a[0] = "J" #불가능, 에러 발생
print(type(a[0]))

#문자열 메소드로 변경해도 원본은 그대로, 새로운 문자열 객체가 생성됨
b = a.upper()

print(a, b)
print(id(a), id(b))
print(a is b) # a, b는 서로 다른 객체이다.

#문자열 연결시 + 연산도 새로운 문자열 객체를 만듦
a = "Hello"
print(id(a))
a += "Python"
print(id(a))

#문자열 vs 리스트 실행 시간 테스트
import time

my_str = ""

start = time.time()
for i in range(1000):
    my_str += str(i)
end = time.time()

#print(my_str) #너무 길어서 생략
print(f"실행 시간: {end - start:.6f}초")

my_list = []

start = time.time()
for i in range(1000):
    my_list.append(str(i))

s = "".join(my_list)
end = time.time()

#print(my_list) #너무 길어서 생략(2)
print(f"실행 시간: {end - start:.6f}초")

# 문자열은 반복 가능함: Iterable

s = "Python"

for ch in s:
    print(ch, end = " ")
print()

##Irerator에 의해 반복 처리
it = iter(s) #문자열(Iterable)에 iter()를 호출하면 Iterator 객체가 생성됨
print(next(it)) #인덱스 0을 반환하고, 다음 위치(인덱스 1)로 이동
print(next(it)) #인덱스 1을 반환하고, 다음 위치(인덱스 2)로 이동
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#print(next(it)) #초과하면 오류남

# 같은 Iterable 데이터 타입인 리스트로 변환 가능
print(list(s))

#문자열 언팩팅도 가능
a, b, c, d, e, f = s
print(a, b, c, d, e, f, sep = "") #개수가 정확하지 않으면 에러남

#확장 언팩킹
a, *b, c = s #나머지를 b에 저장
print(a, b, c) 

#문자열은 순서가 있다: sequence

a = "Python"

#인덱싱
print(a[0])
print(type(a[0]))
print(a[len(a) - 1])
print(a[-1])
print(id(a[0]), id(a[0]))
print(id(a[0]))

# 슬라이싱 (start:end-1:step)
print(a[0:2]) #step은 생략하면 1
print(a[:2]) #start는 생략하면 0
print(a[2:6:1])
print(a[2:4:1])

print(a[::1])
print(a[0:6:1])
print(a[::2])

print(a[::-1])
print(a[2:6:-1]) #start가 엔드보다 스텝이 음수일 때, 더 작아 작동 안됨
print(a[5:1:-1])

#인덱싱과 슬라이싱 차이
#print(a[100]) 인덱스 에러 발생