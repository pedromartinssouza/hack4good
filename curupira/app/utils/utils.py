from pyowm.owm import OWM
owm = OWM('df60f155083559993c09dbf65eda2992')

def getWeatherData(lat, longit):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_coords(lat, longit) 
    weather = observation.weather

    return (weather.temperature(), weather.humidity, weather.wind())
