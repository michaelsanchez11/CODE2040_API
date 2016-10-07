#Problem: With a given dictionary with a prefix and elements, send an array with words without the given prefix

#imported requests and ast for request and static casting the unicode request to a dictionary
import requests
import ast

#requested call
requestCall = {'token': '003a7f4e7bc0a73620257a90a5c6bc51'}

#receiving the request 
dictionary = requests.post('http://challenge.code2040.org/api/prefix',json = requestCall)

#printing the request content
#print dictionary.text

#convert the uncode request to a dictionary
fixedDict = ast.literal_eval(dictionary.text)

#saved the prefix in as a string
prefix = fixedDict[fixedDict.keys()[0]]

#saved the length of the prefix
length = len(prefix)

#our final array result
finalArray = []

#printing the dictionary
print fixedDict
print '\n' 

#the for loop if traversing through the array in out dictionary
for i in range(len(fixedDict['array'])):
	#if condition if checking if the prefix is present or not
    if prefix != fixedDict['array'][i][:length]:
    	#if prefix is not present in string, input to our finalArray result
    	finalArray.append(fixedDict['array'][i])

#printing the results
print finalArray
print prefix





