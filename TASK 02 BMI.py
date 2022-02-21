mass = float(input("Enter your mass: "))
height = float(input("Enter your height: "))

BMI = mass/height**2


if (BMI < 18.5 ):
    print(str(BMI) + " => Under Weight")

elif (BMI >= 18.5 and BMI < 25):
    print(str(BMI) + " => Healthy Weight")
    
elif(BMI >= 25 and BMI < 30):
    print(str(BMI) + " => OverWeight")

else:
    print(str(BMI) + " => Obesity Weight")
