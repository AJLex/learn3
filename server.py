from flask import Flask
from weather import get_weather
from datetime import datetime

city = 'Moscow'
api_key = '99c55e2d754cea316b7aab639531eb6d'
app = Flask(__name__)

@app.route("/")
def index():
    cur_time = datetime.now().strftime('%d.%m.%Y')
    url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s&units=metric' %(city, api_key)
    weather = get_weather(url)
    result = "<p><b>Температура:</b> %s</p>" %(weather['main']['temp'])
    result +="<p><b>Город:</b> %s</p>" %(weather['name'])
    result += "<p><b>Время:</b> %s</p>" %(cur_time)
    return result

if __name__ == '__main__':
    app.run()
