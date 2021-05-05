#print("Palindrome Code")
string = input("Your name: \n").upper()
print("Palindrome" if string == string[::-1] else "Not palindrome")
#print("Palindrome" if input("Your name: \n").upper() == [::-1] else "Not palindrome")

