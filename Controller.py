import datetime

from fastapi import FastAPI, HTTPException

from typing import List

from models.Student import Student
from models.Course import Course
from models.Lecturer import Lecturer
from models.HomeWork import HomeWork
from models.HomeWorkAssignment import HomeWorkAssignment


app = FastAPI()


students_ = {
    1: Student(id=1, full_name='Pavel Egipti', courses=[1, 2], home_work_assignment_ids=[1]),
    2: Student(id=2, full_name='Nikita Khramov', courses=[], home_work_assignment_ids=[]),
    3: Student(id=3, full_name='Daniel Gabitov', courses=[2], home_work_assignment_ids=[]),
}

lecturers_ = {
    1: Lecturer(id=1, full_name='Anton Kuznetsov', courses=[1]),
    2: Lecturer(id=2, full_name='Yuriy Litvinov', courses=[2])
}

courses_ = {
    1: Course(id=1, lecturer_id=1, student_ids=[1], home_work_ids=[1],  name='simple_name', info='simple_info'),
    2: Course(id=2, lecturer_id=2, student_ids=[1, 3], home_work_ids=[], name='another_simple_name', info='another_simple_info')
}

home_works_ = {
    1: HomeWork(id=1, course_id=1, home_work_assignment_ids=[1], name='simple-dimple', description='239', deadline=datetime.datetime.now())
}

home_work_assignments_ = {
    1: HomeWorkAssignment(id=1, home_work_id=1, student_id=1, date=datetime.datetime.now(), mark=9, review_message=None)
}


@app.get("/students", response_model=List[Student])
async def students():
    return list(students_.values())


@app.get("/students/{student_id}", response_model=List[Student])
async def student_by_id(student_id: int):
    if student_id not in students_:
        return HTTPException(status_code=404, detail=f'Could not find student with id={student_id}')
    return students_[student_id]


@app.get("/courses", response_model=List[Course])
async def courses():
    return courses_.values()


@app.get("/courses/{course_id}", response_model=Course)
async def course_by_id(course_id: int):
    if course_id not in courses_:
        return HTTPException(status_code=404, detail=f'Could not find course with id={course_id}')
    return courses_[course_id]


@app.get("/homeworks", response_model=List[HomeWork])
async def homeworks():
    return home_works_.values()


@app.get("/homeworks/{home_work_id}", response_model=List[HomeWork])
async def homework_by_id(home_work_id: int):
    if home_work_id not in home_works_:
        return HTTPException(status_code=404, detail=f'Could not find homework with id={home_work_id}')
    return home_works_[home_work_id]


@app.get("/homeworksAssignments/{home_work_assignment_id}", response_model=List[HomeWorkAssignment])
async def homeworks_assignments_by_id(home_work_assignment_id: int):
    if home_work_assignment_id not in home_work_assignments_:
        return HTTPException(
            status_code=404, detail=f'Could not find home_work_assignment with id={home_work_assignment_id}')
    return home_work_assignments_[home_work_assignment_id]

