# example of dataclasses
from dataclasses import dataclass

@dataclass
class Example():
    """ This is an example class for dataclass notes """
    name: str
    age: int
    height: float
    alive: bool

test = Example('Brian', 30, 75.5, True)

print(test)

