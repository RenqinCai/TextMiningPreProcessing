import json
import os

class _ParentDoc:
	def __init__(self):
		self.m_fileName = "" ###index
		self.m_name = ""  ##string
		self.m_title = ""
		self.m_content = ""
		self.m_parent = ""
		self.m_childList = []
		self.m_jsonHashMap = {}
		self.m_sentences = ""

	def addChild(self, childName):
		if childName not in self.m_childList:
			self.m_childList.append(childName)

	def transformToJson(self):
		self.m_jsonHashMap.setdefault("name", self.m_fileName)
		self.m_jsonHashMap.setdefault("title", self.m_title)
		self.m_jsonHashMap.setdefault("sentences", self.m_sentences)
		self.m_jsonHashMap.setdefault("content", self.m_content)
		self.m_jsonHashMap.setdefault("parent", self.m_parent)
		
		childNames = ""
		for child in self.m_childList:
			childNames += child
			childNames += "\t"

		self.m_jsonHashMap.setdefault("child", childNames)

class _ChildDoc:
	def __init__(self):
		self.m_name = ""
		self.m_title = ""
		self.m_content = ""
		self.m_parent = ""
		self.m_childList = []
		self.m_jsonHashMap = {}
		self.m_sentences=""

	def transformToJson(self):
		self.m_jsonHashMap.setdefault("name", self.m_name)
		self.m_jsonHashMap.setdefault("title", self.m_title)
		self.m_jsonHashMap.setdefault("sentences", self.m_sentences)
		self.m_jsonHashMap.setdefault("content", self.m_content)
		self.m_jsonHashMap.setdefault("parent", self.m_parent)
		
		childNames = ""
		for child in self.m_childList:
			childNames += child
			childNames += "\t"

		self.m_jsonHashMap.setdefault("child", childNames)

class _Corpus:
	def __init__(self):
		##parentName:parentObj
		self.m_parentMap = {}
		self.m_childMap = {}

	def addParent(self, parentName, parentObj): 
		self.m_parentMap.setdefault(parentName, parentObj)

	def addChild(self, childName, childObj):
		self.m_childMap.setdefault(childName, childObj)

	def getParentDocSize(self):
		parentDocSize = len(self.m_parentMap)
		print "the number of parent doc is\t", parentDocSize
		return parentDocSize

	def getChildDocSize(self):
		childDocSize = len(self.m_childMap)
		print "the total number of child doc is\t", childDocSize
		return childDocSize

def loadParentFile(fileName, corpusObj):
	f = open(fileName)

	for rawLine in f:
		jsonData = json.loads(rawLine)
		APPName = jsonData["app_id"]
		APPDescription = jsonData["description"]

		if APPName in corpusObj.m_parentMap.keys():
			continue
		parentObj = _ParentDoc()
		parentObj.m_name = APPName
		parentObj.m_fileName = str(len(corpusObj.m_parentMap))
		# print parentObj.m_fileName
		parentObj.m_content = APPDescription

		corpusObj.m_parentMap.setdefault(APPName, parentObj)

	f.close()


def loadChildFile(fileName, corpusObj):
	f = open(fileName)

	for rawLine in f:
		jsonData = json.loads(rawLine)
		APPReview = jsonData["reviews"]
		APPName = jsonData["app_id"]

		if APPName not in corpusObj.m_parentMap.keys():
			print "no parent doc in corpus for this child"
			continue

		parentObj = corpusObj.m_parentMap[APPName]
		parentFileName = parentObj.m_fileName

		# childList = parentObj.m_childList
		# childSize = len(childList)

		reviewLen = len(APPReview)
		print "reviewLen\t", reviewLen
		for i in range(reviewLen):
			childObj = _ChildDoc()
			childName = parentFileName+"_"+str(i)
			childObj.m_name = childName
			childObj.m_content = APPReview[i]

			parentObj.addChild(childName)
			childObj.m_parent = parentFileName
			corpusObj.m_childMap.setdefault(childName, childObj)

	f.close()

def writeChildFile(dirName, corpusObj):
	for childName in corpusObj.m_childMap.keys():
		jsonFile = open(os.path.join(dirName, "%s.json"%childName), "w")
		childObj = corpusObj.m_childMap[childName]
		childObj.transformToJson()
		json.dump(childObj.m_jsonHashMap, jsonFile)
		jsonFile.close()

def writeParentFile(dirName, corpusObj):
	for parentName in corpusObj.m_parentMap.keys():
		parentObj = corpusObj.m_parentMap[parentName]
		jsonFile = open(os.path.join(dirName, "%s.json"%parentObj.m_fileName), "w")
		parentObj.transformToJson()
		json.dump(parentObj.m_jsonHashMap, jsonFile)
		jsonFile.close()

parentFile = "../../Data/TextMiningProject/appsearch_data/apps_all"
childFile = "../../Data/TextMiningProject/appsearch_reviews/appsearch_reviews.txt"

parentDir = "../../Data/TextMiningProject/APPDescriptions"
childDir = "../../Data/TextMiningProject/APPReviews"

corpusObj = _Corpus()

loadParentFile(parentFile, corpusObj)
loadChildFile(childFile, corpusObj)

writeParentFile(parentDir, corpusObj)
writeChildFile(childDir, corpusObj)


