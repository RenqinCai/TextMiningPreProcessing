class _Query:
	def __init__(self):
		m_queryID = 0
		m_querySource = ""
		m_relevantAPP = []


def loadFile(fileName, queryList, queryMap):
	f = open(fileName)

	for rawLine in f:
		line = rawLine.strip().split("\t")
		query = line[0]
		relevantAPP = line[1]
		relevance = line[2]

		if query not in queryList:
			queryList.append(query)

		if query not in queryMap.keys():
			queryMap.setdefault(query, [])
			queryMap[query].append(rawLine)
		else:
			queryMap[query].append(rawLine)

def writeQueryIDFile(fileName, queryList, queryMap):
	f = open(fileName, "w")

	for i in range(len(queryList)):
		query = queryList[i]
		f.write(str(i)+"\t"+query+"\n") 

	f.close()

def writeQuerySourceFile(fileName, queryList, queryMap):
	f = open(fileName, "w")

	for i in range(len(queryList)):
		query = queryList[i]

		queryLineList = queryMap[query]

		for queryLine in queryLineList:
			f.write(str(i)+"\t"+queryLine)

	f.close()

queryMap = {}
queryList = []

inputFileName = "../../../Data/TextMiningProject/appsearch_data/query-app-relevance"

loadFile(inputFileName, queryList, queryMap)

queryIDFileName = "./queryID.txt"
querySourceFileName = "./query-app-relevance.txt"

writeQueryIDFile(queryIDFileName, queryList, queryMap)
writeQuerySourceFile(querySourceFileName, queryList, queryMap)
