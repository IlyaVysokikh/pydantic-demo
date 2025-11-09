from functools import cached_property
import random
from pydantic import BaseModel, computed_field

class Square(BaseModel):
    width: float
    
    @computed_field
    @property
    def area(self) -> float:
        return self.width ** 2
    
    @area.setter
    def area(self, new_area: float) -> None:
        self.width = new_area ** 0.5
        
    @computed_field(alias='the magic number', repr=False)
    @cached_property
    def random_number(self) -> int:
        return random.randint(0, 1000)
    
square = Square(width=2.0)
print(repr(square))

print(square.random_number)

print(square.model_dump())

square.area = 1.69

print(square.model_dump_json(by_alias=True))
