#Check the text 
text=input("Enter your text")
def spaces(x):
		lis=[0]
		for i in range(len(x)):
			if x[i].isspace():
				lis.append(i)
				lis[0]+=1
		return (f"number of spaces :{lis[0]},index of spaces : {lis[1:]}")
		
def check(text):
	length=len(text)
	num=[0]
	str=[0]
	symbol=[0]
	inde=0
	space=spaces(text)
	for i in text:
		if i.isnumeric():
			num.append(int(i))
			num[0]=num[0]+1
		elif i.isalpha():
			str.append(i)
			str[0]=str[0]+1
		elif i.isspace():
			pass
		else:
			symbol.append(i)
			symbol[0]=symbol[0]+1
	return (f"length of text : {length} \nCount of number : {num[0]} ,numbers : {num[1:]} ,\n Count of alphabet : {str[0]} , strings : {str[1:] }\n Count of symbols :{symbol[0]} , symbols : {symbol[1:]} \n spaces: {space}")
print(check(text))
	