# Validata
dataclass & validation simple as well as hell. 

## install
```bash
pip install validata
```
with github
```
git clone https://github.com/MirS0bhan/validata && cd validata
pip install .
```

## usage 
```python
from validata import BaseModel

class A(BaseModel):
  x:int
  y:int

class B(A):
  z:list[str]

c = B(5, 6, ["abc", "xyz"])
```

