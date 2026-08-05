# โปรแกรมเพื่อการตรวจสอบผลการสอบ
# ชื่อ : นางสาวอคัมย์สิริ จิตติประวัติ
# รหัสนิสิต : 6830202493


# สร้าง List สำหรับเก็บคะแนน
scores = []

# รับคะแนนนักเรียน 5 คน
for i in range(5):
    exam_score = int(input(f"Enter score of student {i + 1} : "))
    scores.append(exam_score)

print()

# ตรวจสอบผลสอบของนักเรียนแต่ละคน
for i in range(5):
    if scores[i] >= 50:
        print(f"Student {i + 1}: {scores[i]} -> ผ่าน")
    else:
        print(f"Student {i + 1}: {scores[i]} -> ไม่ผ่าน")