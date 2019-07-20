X11=int(input())
if X11!=0:
	print(1,end=' ')
	Y11=1
	Z11=0
	for i in range(1,X11):
		Z11=B11+Y11
		print(Z11,end=' ')
		Z11=Y11
		Y11=B11
else:
	print(0)
