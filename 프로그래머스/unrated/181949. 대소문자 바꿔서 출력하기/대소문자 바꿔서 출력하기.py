str = input()
str1 = ""
for i in range(len(str)):
    if (str[i].isupper()):
        str1 += str[i].lower()
    else:
        str1 += str[i].upper()

print(str1)