import numpy

def loadFile(fileName):
	f = open(fileName)

	queryList = []

	for rawLine in f:
		# print rawLine
		line = rawLine.strip().split(" ")

		keyword1 = line[0]

		if len(line)==2:
			keyword2 = line[1].split("\t")[0]
		else:
			if len(line)==3:
				keyword2 = line[1]+line[2].split("\t")[0]
			else:
				keyword2 = line[1]+line[2]

		query = keyword1+keyword2

		# print query
		if query not in queryList:
			queryList.append(query)

	f.close()

	print "query number \t", len(queryList)
	print queryList

file = "../../Data/TextMiningProject/appsearch_data/query-app-relevance"

loadFile(file)