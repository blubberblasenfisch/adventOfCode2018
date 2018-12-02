with open("input.dat", "r") as inputFile:
    rawInput = inputFile.readlines()
	

occurence = []
maxRange = 2
hits = []
counter = 0

for i in range(0,maxRange+2):
	occurence.append(0)
	
for line in rawInput:
	hits = []
	for letter in set(line):
		counter = line.count(letter)
		if counter < len(occurence):
			hits.append(counter)
	for counter in set(hits):
		occurence[counter] += 1
		
solution = occurence[2]*occurence[3]
print(solution)

#part 2
for line in rawInput:
	for compareLine in rawInput:
		deviation = 0
		for i in range(len(line)-1):
			if line[i] != compareLine[i]:
				deviation += 1
		if deviation == 1:
			solution2 = ""
			for i in range(len(line)-1):
				if line[i] == compareLine[i]:
					solution2 += line[i]
					
print(solution2)
input()
