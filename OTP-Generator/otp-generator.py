import random as ran

otp=""

for i in range(0,4):
	otp = otp + str(ran.randint(0,9))


print("OTP",otp)
