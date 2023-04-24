import random

#define characters

lower = "abcdefghijklmopqstuvwxyz"
upper = "ABCDEFGHIJKLMOPQSTUVWXYZ"
numbers = "0123456789"
symbols = "!@^#$%*£"
string = lower + upper + numbers + symbols
#password length
length = 20 


#generating the random password

password = "".join(random.sample(string,length))

#the result

print ("Your password is: " + password)

