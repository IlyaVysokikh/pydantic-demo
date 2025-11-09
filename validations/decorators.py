from typing import Annotated
from pydantic import validate_call, StringConstraints

@validate_call
def greet_user(name: str, greeting: str = 'Hello') -> str:
    return f'{greeting}, {name}!'

print(greet_user('Ivan'))
print(greet_user(123))

@validate_call
def greet_user_new(name: Annotated[str, StringConstraints(min_length=10)], greeting: str = 'Hello') -> str:
    return f'{greeting}, {name}!'

print(greet_user_new('Ivan'))
