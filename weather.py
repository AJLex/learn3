import requests

def get_weather(url):
	result = requests.get(url)
	if result.status_code == 200:
		return result.json()
	else:
		print("Something wrong")

if __name__ == "__main__":
	data = get_weather("http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=99c55e2d754cea316b7aab639531eb6d")
	print(data)

