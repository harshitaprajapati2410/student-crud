from fastapi import Response
from models.student_model import Student

students = []
id = 0


def get_students_all_controller(response: Response):
    print("Data-->", students)
    response.status_code = 200
    return {
        "message": "Students get Successfully",
        "Students": students
    }


def create_students_controller(student: Student, response: Response):
    global id
    try:
        id += 1
        student.id = id
        students.append(student)
        response.status_code = 201
        return {
            "message": "Student created Successfully",
            "student": student
        }
    except Exception as e:
        print(e)
        response.status_code = 400
        return {
            "message": str(e),
            "isSuccess": False
        }


def get_students_controller(studentid: int, response: Response):
    try:
        for student in students:
            if student.id == studentid:
                response.status_code = 200
                return {
                    "message": student,
                    "isSuccess": True
                }
        response.status_code = 404
        return {
            "message": "Student Not found",
            "isSuccess": False
        }
    except Exception as e:
        print(e)
        response.status_code = 500
        return {
            "message": "Error Fetching student",
            "isSuccess": False
        }


def update_students_controller(
    studentid: int,
    student: Student,
    response: Response
):
    try:
        for index in range(len(students)):
            if students[index].id == studentid:
                student.id = studentid
                students[index] = student
                response.status_code = 200
                return {
                    "message": "Student updated Successfully",
                    "student": student,
                    "isSuccess": True
                }
        response.status_code = 404
        return {
            "message": "Student Not found",
            "isSuccess": False
        }
    except Exception as e:
        print(e)
        response.status_code = 500
        return {
            "message": "Error Updating student",
            "isSuccess": False
        }


def delete_students_controller(studentid: int, response: Response):
    try:
        for index in range(len(students)):
            if students[index].id == studentid:
                students.pop(index)
                response.status_code = 204
                return
        response.status_code = 404
        return {
            "message": "Student Not found",
            "isSuccess": False
        }
    except Exception as e:
        print(e)
        response.status_code = 500
        return {
            "message": "Error Deleting student",
            "isSuccess": False
        }