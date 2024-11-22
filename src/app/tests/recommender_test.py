import pytest
from unittest.mock import patch
from app.api.donuts import get_all_donuts
from app.api.recommender import recommend_next_donut

# @patch()
def test_recommender():
    donuts = get_all_donuts()
    available_donuts = list(map(lambda x: x.name, donuts.root))
    assert 'Maple Bar' == recommend_next_donut(available_donuts)


if __name__ == '__main__':
    pytest.main()



