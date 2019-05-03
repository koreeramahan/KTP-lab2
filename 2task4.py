str = input('Строка:\n')
new1=''
new2=''

for char in str:
    if char.isalpha():
        new1 = new1+char
    if char.isdigit():
        new2 = new2+char

print('Строка с буквами:\n',new1)
print('Строка с цифрами:\n',new2)
