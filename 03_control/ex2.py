# 반복문: while문, for문

# while문 
# 1 ~ 10까지 반복 출력
i = 1
while i <= 10:
    print(i)
    i += 1
    # if i == 6: 
        # break #강제 종료시 else가 실행되지 않음
else:
    print("End")

nums = [1, 3, 4, 7, 9]
target = 2
i = 0
while i < len(nums):
    if target == nums[i]:
        print(f"{target} found")
        break
    i += 1
else:
    print(f"{target} not found")

# 1부터 10까지의 합 구하기
i = 1
tot = 0
while i <= 10:
    tot += i
    i += 1
print(f"total is {tot}")

i = 1
tot = 0
while i <= 10:
    if i % 2 == 0:
        tot += i
    i += 1
print(f"total is {tot}")

i = 1
tot = 0
while i <= 10:
    if i % 2 == 1:
        i += 1
        continue
    tot += i
    i += 1
print(f"total is {tot}")
