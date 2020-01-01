"""
Implements the available weather endpoints that will be used by the bot

We use the free Open Weather Map API: https://rapidapi.com/community/api/open-weather-map
"""
import asyncio
import json

import httpx

import settings


class WeatherApi:
    def __init__(self):
        self._url = settings.WEATHER_API_URL
        self._headers = {
            'x-rapidapi-host': settings.X_RAPIDAPI_HOST,
            'x-rapidapi-key': settings.X_RAPIDAPI_KEY
        }


    async def get_current_weather_data(self, q_str, **kwargs):
        params = kwargs
        params['q'] = q_str

        response = await httpx.get(self._url, params=params, headers=self._headers)
        return response.json()


async def main():
    api = WeatherApi()
    response = await api.get_current_weather_data('ottawa,ca', id=2172797)
    print(f"The current temperature in {response['name']} is {response['main']['temp']}")


if __name__ == '__main__':
    asyncio.run(main())
