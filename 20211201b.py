# AoC 2021 Day 1 Part 2

a=int(0) #num1
b=int(0) #num2
c=int(0) #num3
z=int(0) #num4
d=int(0) #combined
e=int(0) #prevcombined
j=int(0) #puzzleCounter

file = open("puzzleInput.txt", "r") #open puzzle file

for x in file:
	e = d
	z = c
	c = b
	b = a
	a = int(x)
	d = a + b + c
	if z == 0:
		print(str(a) + " N/A")
	else:	
		if d > e: #if new is greater than prev, increase counter
			j = j + 1
			print(str(d) + " INCREASE " + str(j)) 
		else:
			print(str(d) + " DECREASE")  
	
file.close() #close the file

print("Total number of increases: " + str(j))	 	