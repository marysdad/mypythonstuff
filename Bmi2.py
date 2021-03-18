print("This is a BMI calculator.")

weight = float(input("Enter your weight in kg"))

height = float(input("Enter your height in meters"))

bmi = round(weight / (height * height))

if bmi < 18.5:
    print(f"Your BMI is {bmi} and You arfe underweight")
elif bmi > 18.5 and bmi < 25:
    print(f"Your BMI is {bmi} and You are normal weight")
elif bmi > 25 and bmi < 30:
    print(f"Your BMI is {bmi} and You are overweight")
elif bmi > 30 and bmi > 35:
    print(f"Your BMI is {bmi} and You are obese")
else:
    print(f"Your BMI is {bmi} and You are clinically obese")