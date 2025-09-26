from pydantic import BaseModel
from typing import Optional

# Input schema for creating a todo
class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None

# Input schema for updating a todo
class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

# Output schema
class TodoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool

    class Config:
        from_attributes = True   # allow SQLAlchemy objects
