import os

def loadFile(fileName, outputDir):

	outputFileIndex = 0

	f = open(fileName)
	for rawLine in f:

		outputFile = open(os.path.join(outputDir, "%s.json"%outputFileIndex), "w")
		line = rawLine.strip()
		outputFile.write(line)
		outputFile.close()
		outputFileIndex += 1

	f.close()

inputFileName = "../../Data/TextMiningProject/appsearch_data/apps_all"

outputDir = "../../Data/TextMiningProject/descriptionJson/"
loadFile(inputFileName, outputDir)