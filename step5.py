#Problem: Solve the dating game, by adding the seconds to the date and returning the new date. 

#import requests for the json request
#import ast to change from unicode to ascii dictionary
#import datetime to use the date time functions and object
import requests
import ast
import datetime

#requested call
requestCall = {'token': '003a7f4e7bc0a73620257a90a5c6bc51'}

#receiving the request 
dictionary = requests.post('http://challenge.code2040.org/api/dating',json = requestCall)

#print the request info
#print dictionary.text


#convert the uncode request to a dictionary
timeDict = ast.literal_eval(dictionary.text)

#avoided these because of the conflicting data types 'str' and date object .
######################################
#interval = timeDict[timeDict.keys()[1]]
#pulling the time away from the dictionary
#time = timeDict[timeDict.keys()[0]]
######################################


#printing the view the prelim test
#print time
#print interval

#have the string format for the time
timeFormat = '%Y-%m-%dT%H:%M:%SZ'
    
#Grabbing the date and the interval seconds
date = timeDict['datestamp']
interval = timeDict['interval']
  
#print date
#print interval
 
#grabbing the time from the string in our time
time = datetime.datetime.strptime(date, timeFormat)
  
#Adding the seconds to the time
interval = long(interval)
time = time + datetime.timedelta(seconds = interval)
finalTime = time.isoformat()
finalTime = str(finalTime) + 'Z'
 
#printing the final time result
#print finalTime


#finalAnswer if being placed in a dictionary
finalAnswer = {'token': '003a7f4e7bc0a73620257a90a5c6bc51', 'datestamp': finalTime}
  
#finalResult is setn via json
finalResult = requests.post('http://challenge.code2040.org/api/dating/validate', json=finalAnswer)
  
#printing the result
#print finalResult.text 












	#