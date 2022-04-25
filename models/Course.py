from typing import List, Dict
from pydantic import BaseModel


class Course(BaseModel):
    id: int
    lecturer_id: int
    student_ids: List[int]
    home_work_ids: List[int]
    name: str
    info: str
