#FAV Number creating

import time
print("So...")
time.sleep(2)
print("Let's get down to business.")
time.sleep(2)
favnum = int(input("What is your favorite number? "))
time.sleep(2)
print("Ok.")
time.sleep(1)
print("That's a good one.")
x = 0
while favnum > x:
    print(x)
    x = x + 1
time.sleep(2)
def even(favnum):
    if favnum%2 == 0:
        print ("Your favorite number is even")
    else:
        print ("Your favorite number is odd")
even(favnum)
time.sleep(2)
def inter(favnum):
    if favnum < 10:
        print("Interesting that you chose a number less than 10.")
    else:
        print("Interesting that you chose a number more than 10.")
inter(favnum)
time.sleep(2)
if favnum > 0:
    print("Also Interesting that you chose a nonzero, positive number.")
elif favnum == 0:
    print("Wow, you chose the number zero, few people do that.")
else:
    print("I can't believe you chose a negative number, how cool.")
time.sleep(2)
print("...and your number multiplied by itself is: ")
time.sleep(2)
print(favnum**2)
time.sleep(3)
print("The square root of your favorite number is: ")
time.sleep(2)
print(favnum**.5)
time.sleep(3)
print("Not to mention that " + str(favnum) + " is pretty cool")
time.sleep(2)
print ("If you walked " + str(favnum) + " miles that would equal " + str(favnum *1.60934) + " kilometers")
time.sleep(2)
print (str(favnum) + " acres would equal " + str(favnum *43560) + " square feet")
time.sleep(2)
print (str(favnum) + " gallons of water would equal " + str(favnum * 8.43) + " pounds")
time.sleep(2)
print (str(favnum) + " inches would equal " + str(favnum * 25.4) + " square feet")
time.sleep(2)
print (str(favnum) + " feet would equal " + str(favnum * .3048) + " meters")
time.sleep(2)
print (str(favnum) + " miles would equal " + str(favnum * 5280) + " feet")
time.sleep(2)
print (str(favnum) + " degrees Fahrenheit would equal " + str((favnum -32) *(5/9)) + " degrees Celsius")
time.sleep(2)
print (str(favnum) + " degrees Fahrenheit would equal " + str((favnum -32) *(5/9) +273.15) + " degrees Kelvin")
time.sleep(2)
print ("Thanks for listening. I love numbers and it was fun thinking about your favorite number")
time.sleep(5)
while favnum < 10:
    print(favnum)
    favnum = favnum + 1
