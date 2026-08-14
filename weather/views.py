from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
import requests
from core.settings import WEATHER_API_KEY
from django.core.cache import cache
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

@api_view(['GET'])
@throttle_classes([AnonRateThrottle, UserRateThrottle])
def weather(request):
    city = request.query_params.get('city')
    if not city:
        return Response({"Ошибка: город не указан"}, status = 400)
    
    cache_key = f"weather_{city.lower()}"
    cached_data = cache.get(cache_key)
    if cached_data:
        cached_data['source'] = 'cache'
        return Response(cached_data)
    
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={WEATHER_API_KEY}&contentType=json"
    response = requests.get(url)
    if response.status_code != 200:
        return Response({"Ошибка": f"Не удалось получить погоду для {city}"}, status=404)
    
    data = response.json() 
    result = {
        "city" : city,
        "temp" : data['currentConditions']['temp'],
        "conditions" : data['currentConditions']['conditions'],
        "humidity": data['currentConditions']['humidity'],
        "description" : data['description']
    }
    cache.set(cache_key, result, timeout=600)
    result['source'] = 'API'
    return Response(result)
    