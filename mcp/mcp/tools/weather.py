from services.weather_service import get_weather

def run(params):

    city = params["city"]

    return get_weather(city)