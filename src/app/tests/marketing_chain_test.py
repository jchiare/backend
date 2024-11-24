import pytest
from app.chain.marketing_chain import create_new_donut_names
from app.api.donuts import get_all_donuts


def test_create_new_donut_names():

    existing_donuts = get_all_donuts()
    existing_donuts_names = [donut.name for donut in existing_donuts.root]

    ai_generated_donut_names = create_new_donut_names(existing_donuts_names)

    assert isinstance(ai_generated_donut_names, list), "Function should return a list"
    assert (
        len(ai_generated_donut_names) == 5
    ), "Function should return 5 new donut names"

    substring_found = False
    for existing_donut_name in existing_donuts_names:
        for new_name in ai_generated_donut_names:
            if existing_donut_name in new_name:
                substring_found = True
                print(
                    f"Found existing donut name '{existing_donut_name}' in new name '{new_name}'"
                )
                break
        if substring_found:
            break

    assert (
        substring_found
    ), "At least one new name should contain a substring from existing donuts"


test_create_new_donut_names()
