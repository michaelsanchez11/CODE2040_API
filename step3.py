#Problem: Find the needle in the haystack

#using requests because of the json post communication 
import requests
#using ast to convert the unicode request into a dictionary
import ast

#request call
requestCall = {'token': '003a7f4e7bc0a73620257a90a5c6bc51'}

#grabbing the request
dictionary = requests.post('http://challenge.code2040.org/api/haystack', json = requestCall)

#convertion from unicode to dict
haystackDict = ast.literal_eval(dictionary.text)

#saved the needle in as a string
needle = haystackDict[haystackDict.keys()[1]]

#retrieved and saved the index value of the needle in the haystack
indexval = haystackDict["haystack"].index(needle)

#prints the index of the found value
print indexval


