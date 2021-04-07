import eel
import pyowm

owm = pyowm.OWM("Your number for weather.app")

@eel.expose



def get_weather(place):

    city = place
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(city)

    w = observation.weather

    temp = w.temperature('celsius')['temp']

    return "В городе " + city + " сейчас " + str(temp) + " градусов!"



eel.init("web")

eel.start("main.html", size=(700, 700))



