# Validata

Dataclass and validation made simple as well as powerful.

## Installation

You can install **Validata** using pip:

```bash
pip install validata
```
To install from GitHub:

```bash
git clone https://github.com/MirS0bhan/validata && cd validata
pip install .
```
## Usage
### Basic Example

Here’s how to define a dataclass and use the validation features:
```python
from vlidt import BaseModel

class A(BaseModel):
    x: int
    y: int

class B(A):
    z: list[str]

c = B(5, 6, ["abc", "xyz"])
```
### Validation

You can validate the fields of your dataclass instances easily:
```python
from vlidt import validate

# Validate the instance
is_valid = validate(c)
print(is_valid)  # Returns True if valid, otherwise False
```
### Dumping and Loading Data

You can convert your dataclass instances to and from dictionaries:
```python
# Dumping the instance to a dictionary
data_dict = dump(c)
print(data_dict)  # Output: {'x': 5, 'y': 6, 'z': ['abc', 'xyz']}

# Loading from a dictionary
new_instance = load(B, data_dict)
print(new_instance)  # Output: B(x=5, y=6, z=['abc', 'xyz'])
```
### Nested Dataclasses

Validata supports nested dataclasses, allowing you to create more complex data structures:
```python
class C(BaseModel):
    a: A
    additional_info: str

instance_c = C(a=c, additional_info="Some info")
print(instance_c)
```
#### Features

- Automatic Validation: Validate dataclass fields with minimal effort.
- Dump and Load: Easily convert dataclass instances to and from dictionaries.
- Nested Support: Handle nested dataclass instances seamlessly.
- Type Annotations: Leverage Python’s type hints for better code clarity and error checking.

#### Contributing

Contributions are welcome! If you would like to contribute to Validata, please follow these steps:

- [ ] Fork the repository.
- [ ] Create a new branch for your feature or bugfix.
- [ ] Make your changes and commit them.
- [ ] Push to your branch and submit a pull request.

#### License

This project is licensed under the MIT License. See the LICENSE file for more details.
Contact

For any inquiries or suggestions, feel free to reach out via GitHub Issues.
