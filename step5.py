#Problem: Solve the dating game, by adding the seconds to the date and returning the new date. 

import requests
import ast
import datetime
import dateutil.parser as dp

#requested call
requestCall = {'token': '003a7f4e7bc0a73620257a90a5c6bc51'}

#receiving the request 
dictionary = requests.post('http://challenge.code2040.org/api/dating',json = requestCall)

#print dictionary.text


#convert the uncode request to a dictionary
timeDict = ast.literal_eval(dictionary.text)

#saved the prefix in as a string
interval = timeDict[timeDict.keys()[1]]
#pulling the time away from the dictionary
time = timeDict[timeDict.keys()[0]]

#printing the view the prelim test
print time

print interval

  
  












	#