# 비트 연산자

a = 5 # 0000 0101
b = 3 # 0000 0011
print(a & b) # 비트 and 연산 1 0000 0001
print(a | b) # 비트 or 연산 7 0000 0111
print(a ^ b) # xor 연산 6 0000 0110
print(a << b) # 5 -> 10 -> 20 -> 40
print(40 >> 3) # 5
print(~a) # 1111 1010 -> 2의 보수로 연산 - 0000 0110 = -6

# 멤버쉽 연산자
print("a" in "apple") # True
print(1 in [1, 2, 3]) # True

# 삼항 연산자
# int max = a > b ? a : b #c 형식
max = a if a > b else b #앞이 부합하는 값 뒤가 틀릴 때 넣는 값이다.

# a값이 짝수면 짝수 출력 홀수면 홀수 출력

print(f"{"짝수" if a % 2 == 0 else "홀수"}")

score = 85
# 90점 이상이면 "A"
# 80점 이상이면 "B"
# 70점 이상이먄 "C"
# 70점 미만이면 "D"

print(f"{"A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D"}")