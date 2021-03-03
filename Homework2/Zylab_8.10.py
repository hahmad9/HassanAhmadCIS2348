# Hassan Ahmad
# ID: 1865003

string = input()
normal = ""
reverse = ""

for i in range(len(string)):
    if string[i].isalpha():
        normal += string[i].lower()
        reverse = string[i].lower() + reverse

if normal == reverse:
    print(string + " is a palindrome")
else:
    print(string + " is not a palindrome")
