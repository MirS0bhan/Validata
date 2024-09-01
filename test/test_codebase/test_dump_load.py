import unittest
from typing import List, Optional
from dataclasses import dataclass

# Assuming load and dump are part of your custom implementation
from vlidt import load, dump, BaseModel  # Replace `your_module` with the actual module name


class Address(BaseModel):
    street: str
    city: str
    zipcode: str


class User(BaseModel):
    name: str
    age: int
    address: Address
    friends: List[str]
    email: Optional[str] = None  # Optional field
    phone: Optional[str] = None  # Optional field


class TestSerialization(unittest.TestCase):

    def setUp(self):
        # Base data without optional fields
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

        # Base instance without optional fields(BaseModel)
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
        #self.assertEqual(dumped_data, self.user_data)


    def test_load(self):
        loaded_instance = load(User, self.user_data)
        self.assertEqual(loaded_instance, self.user_instance)

    def test_dump_and_load(self):
        dumped_data = dump(self.user_instance)
        loaded_instance = load(User, dumped_data)
        self.assertEqual(loaded_instance, self.user_instance)

    def test_optional_fields(self):
        # Data with optional fields included
        user_data_with_optional = {
            "name": "John Doe",
            "age": 30,
            "address": {
                "street": "123 Main St",
                "city": "Anytown",
                "zipcode": "12345"
            },
            "friends": ["Alice", "Bob"],
            "email": "john.doe@example.com",
            "phone": "123-456-7890"
        }

        # Instance with optional fields included
        user_instance_with_optional = User(
            name="John Doe",
            age=30,
            address=Address(
                street="123 Main St",
                city="Anytown",
                zipcode="12345"
            ),
            friends=["Alice", "Bob"],
            email="john.doe@example.com",
            phone="123-456-7890"
        )

        # Dump test
        dumped_data = dump(user_instance_with_optional)
        self.assertEqual(dumped_data, user_data_with_optional)

        # Load test
        loaded_instance = load(User, user_data_with_optional)
        self.assertEqual(loaded_instance, user_instance_with_optional)


if __name__ == "__main__":
    unittest.main()
