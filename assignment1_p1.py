#Python program to capitalize the first and last character of each word in a string

def capitalize_first_last_letters(str1):
    str1 = result = str1.title()
    result = ""
    for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
    return result[:-1]
print(capitalize_first_last_letters("umez arfath hasni"))