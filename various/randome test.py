max_x = 10
max_y = 10
course = []

for i in range(max_y+1):
	print("___|"*max_x)
	for j in range(max_x+1):
		course.append((j,i))

#for j in range(max_x+1):
#	print("|\n"*max_y)



#for every three newlines(equal to the number of y values) i want to draw y horizontal lines equal to the length of the terminal - 10

#for every 5 spaces(times the number of x values) i want to draw 
