'''A python code to determine if you are lucky, by taking a user inputted name.
Getting the corresponding value, for A=1, B=2, C=3 and so forth.
Then tuning it into a 1 digit value, say if you got 157, it becomes 1+5+7 = 13 = 1+3 = 4.
Finally checking if the value obtained (4) is a fibonacci series number.
If it is, output: You are Lucky, else output: You are Unlucky.
'''

#'''
def single_digit_function(value):
    sum = 0
    while(value > 0 or sum > 9): # if 157 or 1+5+7 = 13 which is > 9
        if(value == 0): # then reset the values, new value = 13, sum = 0
            value = sum
            sum = 0
        sum += int(value % 10)
        value /= 10
    return int(sum) # cause sum is now < 9 and value = 0 from the division.
#'''

# Obtain User's name
name = input("Your Name: \n").lower().replace(" ","")
print("Your name is: " + name)
# Find the value of the name
val=0
for letter in name:
    val = val+ord(letter)-96
print("The value of your name is: " + str(val))
# Find the Single Digit value
single_digit = single_digit_function(val)
''' For a 0(1) function, use below.
if val % 9 == 0:
    single_digit = 9
else:
    single_digit = val % 9
'''
print("The single digit is: " + str(single_digit))
# Find if Single Digit value is a Fibonacci Series
luck = x = y = 1
if single_digit == 0 or single_digit == 1:
    luck = 0
for i in range(6):
    if single_digit == x + y:
        luck = 0
        break
    temp = x + y
    x = y
    y = temp
# Output if lucky or not
print("Woah, you are Lucky af" if luck == 0 else "Damn, you are so Unlucky")
