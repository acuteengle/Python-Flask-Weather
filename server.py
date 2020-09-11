#pip install requests
import requests

from flask import Flask, render_template, request

from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)

@app.route('/')
def weather_dashboard():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def render_results():

    zipcode = request.form['zipcode']
    api_key = get_api_key()
    
    data = get_weather_results(zipcode, api_key)

    temp = "{0:.2f}".format(data["main"]["temp"])
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    location = data["name"]
    icon = data["weather"][0]["icon"]
    image_url = "http://openweathermap.org/img/wn/{}@2x.png".format(icon)

    return render_template('results.html', location=location, temp=temp, feels_like=feels_like, weather=weather, image_url=image_url)

def get_api_key():
    blah = os.environ['WEATHER_API_KEY']
    return blah

def get_weather_results(zipcode, api_key):
    # api_url = "http://api.openweathermap.org/data/2.5/weather?zip=94110&units=imperial&appid=738162552cd43ec686ab6e741cfa8ff4"
    api_url = "http://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid={}".format(zipcode, api_key)
    result = requests.get(api_url)
    return result.json()

if __name__ == '__main__':
    app.run() 


