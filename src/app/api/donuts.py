import os
import json
import logging
from typing import List
from collections import Counter
from app.api.classes import DonutCollection, Donut
from app.utils.decorator import should_modify

_file_path = f"{os.path.dirname(__file__)}/../../data/data.json"


DONUT = "donut"


@should_modify
def get_all_donuts() -> DonutCollection | None:
    try:
        with open(_file_path, "r") as file:
            data = json.load(file)

        return DonutCollection(
            root=[Donut(**donut) for donut in data if donut.get("type") == DONUT]
        )
    except Exception as e:
        logging.error(f"Error loading donuts: {str(e)}")
        return None


@should_modify
def find_most_common_toppings(donuts: List[Donut], top_n: int) -> List[str]:

    # I find this easier to read then a list comprehension :)
    # Happy to change to the team standard though
    all_toppings = [topping.type for donut in donuts for topping in donut.topping]

    topping_counts = Counter(all_toppings)
    most_common = topping_counts.most_common(top_n)

    return [topping for topping, _ in most_common]
