# Python program to check if a string contains any special character 

String = input('Enter the string :')
count = 0
for i in String:
    if i == '!' or i == '@' or i == '#' or i == '$' or i == '&' or i == '_' or i == '%' :
        count+=1

if count >=1:
    print('string not accepted')
else:
    print('string accepted')