# AOC 2021 Day 1

a=int(0) #newNum
b=int(0) #prevNum
j=int(0) #puzzleCounter

file = open("puzzleInput.txt", "r") #open puzzle file

for x in file:
	b = a #set b to previous number
	a = int(x)
	if b == 0:
		print(str(a) + " N/A")
	else:	
		if a > b: #if new is greater than prev, increase counter
			j = j + 1
			print(str(a) + " INCREASE " + str(j)) 
		else:
			print(str(a) + " DECREASE")  
	
file.close() #close the file

print("Total number of increases: " + str(j))	 	