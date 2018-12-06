with open("input.dat", "r") as inputFile:
    rawInput = inputFile.readlines()

fabric = [[0] * 1000 for i in range(1000)]
	
for line in rawInput:
	tmp = line.split()
	ID = tmp[0][1:]
	xStart = int(tmp[2].split(",")[0])
	yStart = int(tmp[2].split(",")[1][:-1])
	width = int(tmp[3].split("x")[0])
	height = int(tmp[3].split("x")[1])
	for x in range(xStart, xStart+width):
		for y in range(yStart, yStart+height):
			fabric[x][y] += 1

count = 0
for thread in fabric:
	for square in thread:
		if square > 1:
			count += 1

solution = count

###################################
#part 2

fabric = [[0] * 1000 for i in range(1000)]
notTheSolution = []

for line in rawInput:
	tmp = line.split()
	ID = int(tmp[0][1:])
	xStart = int(tmp[2].split(",")[0])
	yStart = int(tmp[2].split(",")[1][:-1])
	width = int(tmp[3].split("x")[0])
	height = int(tmp[3].split("x")[1])
	for x in range(xStart, xStart+width):
		for y in range(yStart, yStart+height):
			if fabric[x][y] > 0:
				notTheSolution.append(ID)
				notTheSolution.append(fabric[x][y])
			fabric[x][y] = ID

IDs = [x for x in range(1, ID+1)]
solution2 =  set(IDs) - set(notTheSolution)

print(solution)
print(solution2)
