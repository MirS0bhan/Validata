import unittest
from typing import List

from vlidt import BaseModel, load, dump


class Address(BaseModel):
    street: str
    city: str
    zipcode: str


class User(BaseModel):
    name: str
    age: int
    address: Address
    friends: List[str]


class TestSerialization(unittest.TestCase):

    def setUp(self):
        self.user_data = {
            "name": "John Doe",
            "age": 30,
            "address": {
                "street": "123 Main St",
                "city": "Anytown",
                "zipcode": "12345"
            },
            "friends": ["Alice", "Bob"]
        }
        self.user_instance = User(
            name="John Doe",
            age=30,
            address=Address(
                street="123 Main St",
                city="Anytown",
                zipcode="12345"
            ),
            friends=["Alice", "Bob"]
        )

    def test_dump(self):
        dumped_data = dump(self.user_instance)
        self.assertEqual(dumped_data, self.user_data)

    def test_load(self):
        loaded_instance = load(User, self.user_data)
        self.assertEqual(loaded_instance, self.user_instance)

    def test_dump_and_load(self):
        dumped_data = dump(self.user_instance)
        loaded_instance = load(User, dumped_data)
        self.assertEqual(loaded_instance, self.user_instance)


if __name__ == "__main__":
    unittest.main()
