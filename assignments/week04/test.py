# รับชื่อจริง (หรือข้อความ) จากผู้ใช้
# นับจำนวนสระทั้งหมดในข้อความนี้ว่ามีกี่ตัว (a, e, i, o, u)
# โดยต้องใช้ loop-for ด้วยเท่านั้น

# ตัวอย่าหน้าจอ
# what is your name?: Boonchoo
# Your text have 4 vowels.


name = input("What is your name?: ")
letters = list(name)
print(letters)

a = letters.count("a")
e = letters.count("e")
i = letters.count("i")
o = letters.count("o")
u = letters.count("u")

A = letters.count("A")
E = letters.count("E")
I = letters.count("I")
O = letters.count("O")
U = letters.count("U")

count = a + e + i + o + u + A + E + I + O + U


count = 0
for letter in name:
    if letter == 'a' or letter == 'A':
        count = count + 1
    elif letter == 'e' or letter == 'E':
        count = count + 1
    elif letter == 'i' or letter == 'I':
        count = count + 1
    elif letter == 'o' or letter == 'I':
        count = count + 1
    elif letter == 'u' or letter == 'U':
        count = count + 1

    
for letter in name:
    if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:   
        count = count + 1

print("Your text have", count, "vowels")