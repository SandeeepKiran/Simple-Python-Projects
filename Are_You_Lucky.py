'''A python code to determine if you are lucky, by taking a user inputted name.
Getting the corresponding value, for A=1, B=2, C=3 and so forth.
Then tuning it into a 1 digit value, say if you got 157, it becomes 1+5+7 = 13 = 1+3 = 4.
Finally checking if the value obtained (4) is a fibonacci series number.
If it is, output: You are Lucky, else output: You are Unlucky.
'''
def SingleDigit(val):
    sum = 0 
    while(sum > 9):

name = input("Your Name: \n").lower()
print(name)
val=0
for letter in name:
    val = val+ord(letter)-96
print(val)

'''
if val>10:
    sum=0
def single_digit(){
    while(val>10 and sum<10):
        sum = sum + int(val % 10)
        val = int(val/10)
        print(sum)
        print(val)
        sum = = sum + int(val % 10)
    return sum 
}
while(sum<10):
    single_digit()
'''
if val < 10:
    sum = val
else:
    sum = SingleDigit(val)
