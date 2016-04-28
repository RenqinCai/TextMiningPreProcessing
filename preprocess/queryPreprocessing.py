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
		queryMap.setdefault(query, rawLine)

def writeQueryIDFile(fileName, queryList, queryMap):
	f = open(fileName)

	for i in range(len(queryList)):
		query = queryList[i]
		f.write(i+"\t"+query+"\n") 

	f.close()

def writeQuerySourceFile(fileName, queryList, queryMap):
	f = open(fileName)

	for i in range(len(queryList)):
		query = queryList[i]

		queryLine = queryMap[query]
		f.write(i+"\t"+queryLine+"\n")

	f.close()

queryMap = {}
queryList = []

inputFileName = "./query-app-relevance"

loadFile(fileName, queryList, queryMap)

queryIDFileName = "./queryID.txt"
querySourceFileName = "./query-app-relevance.txt"

writeQueryIDFile(fileName, queryList, queryMap)
writeQuerySourceFile(querySourceFileName, queryList, queryMap)
