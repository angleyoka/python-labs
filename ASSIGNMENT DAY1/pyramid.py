number=input("enter your number: ")
rang=range(int(number))
for i in rang:
	print(" "*(int(number)-1-i) + "*"*(i+1)) 