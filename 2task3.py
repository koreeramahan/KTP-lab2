import random
import string

str=string.ascii_letters+string.digits
newstr=''
for i in range(8):
	newstr=newstr+random.choice(str)
print ('Сгенерированная строка из букв и цифр = ',newstr)
	
if newstr.isalpha():
        ls=list(newstr)
        ls[random.randint(0,7)]=random.choice(string.digits)
        s=''.join(ls)
        print ('Сгенерированная строка из букв и цифр = ',s)
