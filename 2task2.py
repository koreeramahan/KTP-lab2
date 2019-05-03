list = ['red','plan','risk','dark']
n=0
print ('Слова, начинающиеся с "r":\n')
for i in list:
	if i.startswith('r'):
		print (i)
		n=n+1
if n==0:
	print ('Таких слов не нашлось')
