Weather API

A REST API for retrieving real-time weather data with caching and rate limiting.

Stack:
- Python 3.x
- Django + Django REST Framework
- Visual Crossing Weather API
- Django Cache (LocMemCache)
- JWT Authentication (опционально)

Download:
1. Clone repo:
git clone <URL_ТВОЕГО_РЕПОЗИТОРИЯ>
cd weather_api 

2. Create a virtual environment:
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

3. Install the dependencies:
pip install -r requirements.txt

4. Create a .env file in the project root directory:
WEATHER_API_KEY=your_visual_crossing_api_key

5. Apply migrations (if any):
python manage.py migrate

6. Run server:
python manage.py runserver

API Endpoints:
GET /api/weather/?city=London

Response example:
{
  "city": "London",
  "temp": 22.5,
  "conditions": "Partially cloudy",
  "humidity": 45.2,
  "description": "Similar temperatures continuing with no rain expected.",
  "source": "API"
}

"source" field:
"API" — data retrieved from an external API
"cache" — data from the cache (fast response)

Features:
Integration with the Visual Crossing Weather API
JWT Authentication
10-minute caching (Django cache)
Rate limiting (5 requests/min for anonymous users, 20 for logged-in users)
Error handling (city not specified, city not found)
Automatic city detection by name

[https://github.com/Skkyami/weather-API](https://roadmap.sh/projects/weather-api-wrapper-service)
