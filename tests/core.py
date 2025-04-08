from pydantic import BaseModel

from litestar_forms import Form


class PersonModel(BaseModel):
    name: str
    number: int
    age: int


class PersonForm(Form):
    __model__ = PersonModel



def test_1():
    pf = PersonForm({"name": 1, "age": "a", "number": 1})

    print()





if __name__ == '__main__':
    test_1()