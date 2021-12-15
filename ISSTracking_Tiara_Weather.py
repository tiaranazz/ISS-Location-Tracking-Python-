import requests

#input the city name
#city = 'Malaysia'
city = input('Enter the country/city name')
print(city)

#Display the messages
print('Displaying Weater report for: ' + '' + city)

#Fetch the weather details
url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)

#Display the results
print(res.text)