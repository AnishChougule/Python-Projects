system = input("Choose system Metric(m) or Imperial(i)? ")

def bmi(x, y):
    return round(y / ((x / 100) ** 2),2)

def check_bmi(x):
    if x < 18.5:
        print("You are underweight.")
    elif x < 25:
        print("You are healthy.")
    elif x < 30:
        print("You are overweight.")
    else:
        print("You are obese.")
    print("""\nBMI < 18.5 = Underweight
18.5 < BMI < 25 = Normal weight
25 < BMI < 30 = Overweight
BMI >= 30: Obesity\n""")

try:
    if system == "m":
        height = float(input("Height in cm? "))
        weight = float(input("Weight in kg? "))
        bmi = bmi(height, weight)
        print(f"Your BMI is {bmi}")
        check_bmi(bmi)
    elif system == "i":
        height = float(input("Height in ft? ")) * 30.48
        weight = float(input("Weight in lb? ")) * 0.453592
        bmi = bmi(height, weight)
        print(f"Your BMI is {bmi}")
        check_bmi(bmi)
    else:
        print("Choose the correct option!")
except:
    print("Wrong values!")
