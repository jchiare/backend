import os
import json
import logging
from typing import List
from collections import Counter
from app.api.classes import DonutCollection, Donut
from app.utils.decorator import should_modify

_file_path = f"{os.path.dirname(__file__)}/../../data/data.json"

@should_modify
def get_all_donuts() -> DonutCollection|None:
    raise NotImplementedError("This function is not implemented yet")


@should_modify
def find_most_common_toppings(donuts: List[Donut], top_n) -> list[str]:
    raise NotImplementedError("This function is not implemented yet")
