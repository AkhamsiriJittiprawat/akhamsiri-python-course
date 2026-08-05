# โปรแกรมช่วยตัดสินใจเลือกซื้อสินค้าภายใต้งบประมาณรวม
# ชื่อ : นางสาวอคัมย์สิริ จิตติประวัติ
# รหัสนิสิต : 6830202493


# สร้าง list สำหรับเก็บราคาสินค้า
prices = []

# รับราคาสินค้า 6 ราบการ
print("Enter price of 6 items: ")
for i in range(6):
    price = int(input(f"Item {i + 1}: "))
    prices.append(price)

# รับงบประมาณ
budget = int(input("\nEnter total budget: "))

# ตัวแปรเก็บยอดใช้จ่าย และรายการสินค้าที่ซื้อได้
total = 0
buy_list = []

print()

# ตรวจสอบสินค้าทีละรายการ
for i in range(6):

    # ถ้าซื้อแล้วไม่เกินงบประมาณ
    if total + prices[i] <= budget:
        print(f"Item {i + 1} = {prices[i]} -> buy")

        total = total + prices[i]       # เพิ่มยอด
        buy_list.append(prices[i])      # เก็บรายการที่ซื้อ

    else:
        print(f"Item {i + 1} = {prices[i]} -> cannot buy")

    print(f"Current total = {total}\n")

# แสดงผลลัพธ์
print(f"Bought item: {buy_list}")
print(f"Total spent: {total}")
print(f"Remaining budget : {budget - total}")