from typing import List
from pydantic import BaseModel


class Student(BaseModel):
    id: int
    full_name: str
    courses: List[str]
    home_work_assignment_ids: List[int]
