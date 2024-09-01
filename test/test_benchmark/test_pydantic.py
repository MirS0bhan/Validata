import  pydantic
from typing import List, Optional
from timeit import timeit
import random
import string


# Define the Address and User models
class Address(pydantic.BaseModel):
    street: str
    city: str
    zipcode: str


class User(pydantic.BaseModel):
    name: str
    age: int
    address: Address
    friends: List[str]
    email: Optional[str] = None
    phone: Optional[str] = None


# Helper function to generate random strings
def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))


# Helper function to generate random data for User objects
def generate_random_data(num_objects):
    data = []
    for _ in range(num_objects):
        user_data = {
            "name": random_string(),
            "age": random.randint(18, 80),
            "address": {
                "street": random_string(),
                "city": random_string(),
                "zipcode": random_string(5)
            },
            "friends": [random_string() for _ in range(5)],
            "email": random_string() + "@example.com" if random.choice([True, False]) else None,
            "phone": "".join(random.choices(string.digits, k=10)) if random.choice([True, False]) else None
        }
        data.append(user_data)
    return data


# Function to benchmark the creation of User objects using pre-generated data
def benchmark_user_creation(data):
    for user_data in data:
        user = User(**user_data)


# Run the benchmark
if __name__ == "__main__":
    num_objects = 10000  # Number of User objects to create

    # Generate the random data first
    data = generate_random_data(num_objects)

    # Time the creation of User objects using the pre-generated data
    time_taken = timeit(lambda: benchmark_user_creation(data), number=1)
    print(f"Time taken to create {num_objects} User objects: {time_taken:.2f} seconds")