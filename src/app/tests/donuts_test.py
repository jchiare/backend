import pytest
from app.api.donuts import get_all_donuts, find_most_common_toppings
from app.api.classes import DonutCollection


def test_get_all_donuts():
    donuts = get_all_donuts()
    assert donuts is not None, "Expected a DonutCollection object, got None"
    assert isinstance(
        donuts, DonutCollection
    ), f"Expected type DonutCollection, got {type(donuts)}"
    assert len(donuts.root) == 11, f"Expected 11 donuts, got {len(donuts.root)}"


def test_get_most_common_topping():
    donuts = get_all_donuts()
    assert ["Glazed"] == find_most_common_toppings(donuts.root, 1)
    assert ["Glazed", "Sugar"] == find_most_common_toppings(donuts.root, 2)
    assert ["Glazed", "Sugar", "Maple"] == find_most_common_toppings(donuts.root, 3)


if __name__ == "__main__":
    pytest.main()
