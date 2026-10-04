from fastapi import APIRouter, Response

from controllers.student_controller import (
    create_students_controller,
    get_students_all_controller,
    get_students_controller,
    update_students_controller,
    delete_students_controller
)

from models.student_model import Student


srouter = APIRouter(
    prefix="/students",
    tags=["students"]
)


@srouter.post("/students")
def create_students(student: Student, response: Response):
    return create_students_controller(student, response)


@srouter.get("/students")
def get_students_all(response: Response):
    return get_students_all_controller(response)


@srouter.get("/students/{studentid}")
def get_students(studentid: int, response: Response):
    return get_students_controller(studentid, response)


@srouter.put("/students/{studentid}")
def update_students(studentid: int, student: Student, response: Response):
    return update_students_controller(studentid, student, response)


@srouter.delete("/students/{studentid}")
def delete_students(studentid: int, response: Response):
    return delete_students_controller(studentid, response)