# 조건문: if문, match문

age = 17

if(age >= 18):
    print("성인입니다.")
else:
    print("미성년")

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")

# match 문
grade = "A"

match grade: #파이썬은 브레이크가 자동임
    case "A":
        print("우수")
    case "B":
        print("잘함")
    case "C" | "D": #or 표시 활용 가능
        print("보통")
    case _: #default
        print("알 수 없음")