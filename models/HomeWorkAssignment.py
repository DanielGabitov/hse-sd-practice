import datetime

from pydantic import BaseModel
from typing import Optional


class HomeWorkAssignment(BaseModel):
    id: int
    home_work_id: int
    student_id: int

    date: datetime.datetime
    mark: Optional[int]
    review_message: Optional[str]
