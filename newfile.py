num=int(input("ادخل اساس العدد"))
pow=int(input("ادخل اس العدد"))
def multi(a,b):#دالة الضرب 
	sum=0
	for i in range(a):
		sum+=b
	return sum
def dev(a,b):#دالة القسمة
	sum=0
	if b==0:
		return "الصفر غير معرف في المقام "
	elif a==0:
		return 0
	if a>0:
		while a>0:
			a-=b
			sum+=1
		return sum
	elif a<0:
		while a<0:
			a+=b
			sum+=1
		sum*=-1
		return sum		
def power(num,pow):#دالة الاس 
	po=num
	for i in range(pow-1):
		po=multi(po,num)
	return po
	
	
	
#print(power(num,pow))
print(dev(-10,2))
		