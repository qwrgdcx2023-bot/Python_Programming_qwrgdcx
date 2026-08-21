# 불리언
# True or False
a = True
print(a, type(a), sep = ", ") #True, <class 'bool'>

print(1 < 0, 1 > 0, 1 == 0, 1 != 0, sep = ", ") #False, True, False, True

print("apple" > "banana") #False
print("apple" > "apble") #True

# bool()
print(bool(3)) #True
print(bool(0)) #False
print(bool("Hello, world")) #True
print(bool("")) #False
print(bool(" ")) #True
print(bool([10, 5, 2])) #True
print(bool([])) #False

# None 자료형
a = None
print(a, type(a), sep = ", ") #None, <class 'NoneType'>
print(bool(a)) #False

if a is None:
    print("값이 없습니다.")
    print("행복한 하루 보내세요! :)")


