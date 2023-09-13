import requests

#Change to the command that you want to test
api_command = 'do-stuff'

#Change to the input you want to test
api_input = 'banana'

#Make sure to use the same port that you used in your flask API
response = requests.get('http://localhost:5555/'+ api_command +'/' + api_input)

jsonResponse = response.json()
print(jsonResponse)

print(jsonResponse['stuff'])


