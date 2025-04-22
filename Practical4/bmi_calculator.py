
W = float(input("Imput weight:"))
H = float(input("Imput height:"))
#calculate BMI
H2 = H**2
BMI = W/H2
print ("Your BMI is:",BMI)
#feedback
if BMI > 30:
	print ("You are obese.")
elif BMI < 18.5:
	print ("You are underweight.")
else:
	print ("You have a normal weight.")

