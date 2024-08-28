import unittest
from dataclasses import dataclass
from typing import List, Optional

from validata import BaseModel


# Define a subclass of BaseModel to test the functionality


@dataclass
class Person(BaseModel):
    name: str
    age: int
    hobbies: Optional[List[str]] = None


class TestBaseModel(unittest.TestCase):
    def test_valid_data(self):
        # Test with valid data
        person = Person(name="John", age=30, hobbies=["reading", "cycling"])
        self.assertEqual(person.name, "John")
        self.assertEqual(person.age, 30)
        self.assertEqual(person.hobbies, ["reading", "cycling"])

    def test_invalid_type(self):
        # Test with invalid data (age should be int, not str)
        with self.assertRaises(TypeError):
            person = Person(name="John", age="thirty", hobbies=["reading", "cycling"])

    def test_optional_field(self):
        # Test with None in the optional field
        person = Person(name="Jane", age=25, hobbies=None)
        self.assertEqual(person.name, "Jane")
        self.assertEqual(person.age, 25)
        self.assertIsNone(person.hobbies)

    def test_missing_required_field(self):
        # Test with a missing required field (name)
        with self.assertRaises(TypeError):
            person = Person(age=30, hobbies=["reading", "cycling"])


if __name__ == "__main__":
    unittest.main()
