import requests
#
# url = "https://skyscanner50.p.rapidapi.com/api/v1/searchAirport"
#
# querystring = {"query":"london"}
#
# headers = {
# 	"content-type": "application/octet-stream",
# 	"X-RapidAPI-Key": "ee8fa8e4edmsh4c6fa4956090066p1da508jsn2bb8f8b1c51e",
# 	"X-RapidAPI-Host": "skyscanner50.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())

duomenys = requests.get("https://data.gov.lt/public/api/1/action/package_search")

print(duomenys.text)

