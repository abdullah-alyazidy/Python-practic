thickness=int(input())
c="H"
f=0
for i in range(1,thickness+1):
	print(" "*(thickness-i)+(i)*c+f*c)
	f+=1
for i in range(thickness+1):
	print("  "+thickness*c+" "*thickness*3+thickness*c)
	
for i in range(3):
	print("  "+(thickness*5)*c)

for i in range(thickness+1):
	print("  "+thickness*c+" "*thickness*3+thickness*c)	
	
f2=thickness-1
for i in range(thickness,-1,-1):
	print(" "*(thickness*4)+(" "*(thickness-i))+i*c+f2*c)
	f2-=1