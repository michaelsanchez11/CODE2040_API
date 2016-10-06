#reverse a string
#using requests because of the json post communication 
import requests 

dictionary = {'token': '003a7f4e7bc0a73620257a90a5c6bc51'}

request = requests.post('http://challenge.code2040.org/api/reverse',json = dictionary)

#printed the request to view the string im working with
#print request.text

#converted the request.text as a string
string = request.text

#final result string object is placed in reverseString
reverseString = ''

#grabbed the length of the string input to have my for loop iterate that amount of times when reversing
length = len(string)

#the reversing is done in this for loop
for index in range (0,length):
	#here we place the new character from the string variable concatenated into our reverseString object
	reverseString = string[index] + reverseString

#printing the reverseString for testing purposes	
#print reverseString

#final dictionary to json
finalResult = {'token': '003a7f4e7bc0a73620257a90a5c6bc51' , 'string': reverseString}

#final json post request 
finalRequest = requests.post('http://challenge.code2040.org/api/reverse/validate', json = finalResult)

#print the final result
print finalRequest.text

