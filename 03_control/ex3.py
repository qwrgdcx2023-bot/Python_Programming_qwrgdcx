# for문

# for(int i = 0; i < 10; i ++) // 그립네, 지금은 전시중 접촉 금지
# for i in iterable 객체

for i in range(5):# 0 ~ 4
    print(i, end = "")
print()

a = range(5)
print(a.start,a.stop, a.step)

# 1 ~ 5
for i in range(1, 6, 1):
    print(i, end = "")
print()

# 1 ~ 10, 2씩 띄어서
for i in range(1, 11, 2):
    print(i, end = "")
print()

# 5, 4, 3, 2, 1
for i in range(5, 0, -1):
    print(i, end = "")
print()

# 1 ~ 10까지의 합
tot = 0
for i in range(1, 11, 1):
    tot += i
print(f"tot = {tot}")

print(sum(range(1, 11))) # len이랑 sum은 조낸 쓰니까 꼭 기억하기 

s = "﷼₯₧௹૱₾$↹◈◍◓∭∰ϖϕ"

for c in s:
    print(c, end = " ")
print()

print(len(s))

# 구구단 출력
for i in range(1,10,1):
    for j in range(1, 10, 1):
        print(f"{i} * {j} = {i * j:<5d}", end = "")
    print("")
print("End")


