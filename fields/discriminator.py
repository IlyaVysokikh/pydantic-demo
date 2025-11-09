from typing import Literal

from pydantic import BaseModel, Field


class Cat(BaseModel):
    pet_type: Literal['cat']
    age: int


class Dog(BaseModel):
    pet_type: Literal['dog']
    age: int


class Model(BaseModel):
    pet: Cat | Dog = Field(discriminator='pet_type')


print(Model.model_validate({'pet': {'pet_type': 'cat', 'age': 12}}))
