# AoC 2021 Day 2

horiz=int(0)
aim=int(0)
depth=int(0)
value=int(0)

file = open("puzzleInput.txt", "r") #open puzzle file

for x in file:

	if "forward" in x:
		print(x[x.find(" "):])
		value = x[x.find(" "):]
		horiz = horiz + int(value)
		depth = depth + (int(value)*aim)
	
	elif "down" in x:
		print(x[x.find(" "):])
		value = x[x.find(" "):]
		aim = aim + int(value)
	
	elif "up" in x:
		print(x[x.find(" "):])
		value = x[x.find(" "):]
		aim = aim - int(value)
	
file.close() #close the file

print("Final Value: " + str(depth * horiz))	 	