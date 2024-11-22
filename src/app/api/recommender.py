import requests
from requests.exceptions import HTTPError

from app.utils.decorator import do_not_modify

@do_not_modify
def get_weather_condition_id() -> int:
    response = requests.get("https://api.example.com/weather")
    if response.status_code != 200:
        raise HTTPError(f"Failed to get weather: {response.text}. HttpCode {response.status_code}")
    return response.json()["condition_id"]

@do_not_modify
def recommend_next_donut(available_donuts: list[str]) -> str:
    weather_condition_id = get_weather_condition_id()

    return available_donuts[weather_condition_id % len(available_donuts)]

