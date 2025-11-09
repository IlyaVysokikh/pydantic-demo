from typing import Any
from pydantic import BaseModel, PrivateAttr, ConfigDict

class Cache(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    data: dict[str, Any]
    _hits: int = PrivateAttr(0)
    
    def get(self, key: str) -> Any:
        self._hits += 1
        return self.data.get(key)
        
    
c = Cache(data={"a": 2, "b": 3})
print(c.get("a"))
print(c._hits)
print(c.model_dump())