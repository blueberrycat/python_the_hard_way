def bmi(weight, height):
	print weight/height**2

a = raw_input("Enter your name: ")
b = raw_input("Enter your weight(kg): ")
c = raw_input("Enter your height(m): ")
print "%s's BMI" % a
bmi(float(b), float(c)) 

