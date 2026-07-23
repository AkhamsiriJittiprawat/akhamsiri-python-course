#input
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

#process
BMI = weight / (height ** 2)

if BMI < 18.5:
    category = "Under weight"
elif BMI < 25:
    category = "Nomal weight"
elif BMI < 30:
    category = "Over weight"
else:
    category = "Obese"

#output
print(f"BMI = {BMI:.1f}")   
print("Category: ", category)