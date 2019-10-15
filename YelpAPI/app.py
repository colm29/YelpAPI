import requests
import config

url = 'https://api.yelp.com/v3/businesses/search'
headers = {
    'Authorization': 'Bearer ' + config.API_KEY
}
params = {
    'term': 'bar',
    'location': 'Ballincollig, Cork, Ireland'
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()['businesses']
names = [business['name'] for business in businesses]
print(names)
