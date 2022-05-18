#Exercise 1: Rewrite your pay computation to give the   employee 1.5
#times 
#the hourly rate for hours worked above 40 hours.
hrs = input('Enter hours: ')
h = float(hrs)
rts = input('Enter rate: ')
r = float(rts)

if h <= 40:
        print(h * r)
elif h > 40:
	print (40 * r + (h-40)*1.5*r)
	

#Exercise 2: Rewrite your pay program using try and except so that your
#program handles non-numeric input gracefully by printing a message
#and exiting the program. The following shows two executions of the
#program:

#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input
#Enter Hours: forty
#Error, please enter numeric input

#Executing mine
age = input('Enter age: ')
try:
	int(age)
	weight=input('Enter weight ')
	int(weight)
	pay= int(age) * int(weight)
	print ('pay: ')
except:
	print ('Error, please enter numeric input ')
	
#Exercise 3	
score = float(input("Enter Score: "))
if score >= 0.9:

    print ("A")

elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print ("C")
elif score >= 0.6:
    print ("D")
elif score < 0.6:
    print ("F")
else:
    print ("Error, please enter a number that is in range")
quit()