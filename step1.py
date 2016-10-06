import requests

#dictionary with token and github keys
registration = {'token': '003a7f4e7bc0a73620257a90a5c6bc51', 'github': 'https://github.com/michaelsanchez11/CODE2040_API'}

#the actuall request using post and json
request = requests.post('http://challenge.code2040.org/api/register',json = registration)

#testing the result of the json request
print request.text

