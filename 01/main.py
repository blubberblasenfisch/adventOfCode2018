with open("input.dat", "r") as inputFile:
    rawInput = inputFile.readlines()
	
currentFrequency = 0
knownFrequencies = []
found = False
solution = ""
i=0

while not found:
	i+=1
	for line in rawInput:
		currentFrequency += int(line)
		if currentFrequency in knownFrequencies:
			solution = currentFrequency
			found = True
			break
		knownFrequencies.append(currentFrequency)
	print(i)
	
#print(currentFrequency)
print(solution)
input()
