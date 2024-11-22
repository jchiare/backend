from typing import List
from pydantic import BaseModel, RootModel

class Batter(BaseModel):
    id: str
    type: str

class Batters(BaseModel):
    batter: List[Batter]

class Topping(BaseModel):
    type: str

class Donut(BaseModel):
    id: int
    type: str
    name: str
    ppu: float
    batters: Batters
    topping: List[Topping]

class DonutCollection(RootModel[List[Donut]]):
    pass
