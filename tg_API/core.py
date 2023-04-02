import requests

url = "https://numbersapi.p.rapidapi.com/6/21/date"

querystring = {"fragment":"true","json":"true"}

headers = {
	"X-RapidAPI-Key": site.api_key.get_secret_value(),
	"X-RapidAPI-Host": site.host_api.g
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)