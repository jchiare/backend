import pytest
from unittest.mock import patch
from app.api.donuts import get_all_donuts
from app.api.recommender import recommend_next_donut


@patch("app.api.recommender.get_weather_condition_id")
def test_recommender(get_weather_mock):

    # since the expectation is that we get maple bar
    # and maple bar is the 10th
    # we need to get the 9th element calculate by recommend_next_donut (20 % 11 = 9)
    get_weather_mock.return_value = 20

    # should we mock this at some point?
    donuts = get_all_donuts()
    available_donuts = list(map(lambda x: x.name, donuts.root))
    assert "Maple Bar" == recommend_next_donut(available_donuts)


if __name__ == "__main__":
    pytest.main()
