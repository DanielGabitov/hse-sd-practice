from typing import List
from pydantic import BaseModel


class Lecturer(BaseModel):
    id: int
    full_name: str
    courses: List[int]
