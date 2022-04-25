import datetime

from typing import List
from pydantic import BaseModel


class HomeWork(BaseModel):
    id: int
    course_id: int
    home_work_assignment_ids: List[int]

    name: str
    description: str
    deadline: datetime.datetime
