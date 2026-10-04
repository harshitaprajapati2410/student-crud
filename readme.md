# Student CRUD Application

This is a FastAPI-based Student CRUD application.

## Features

- Create Student
- Get All Students
- Get Student by ID
- Update Student
- Delete Student

## How to Run

Install the required packages:

```bash
pip install fastapi uvicorn
pip install pydantic


for execute the code write this in terminal 
uvicorn main:app --reload

pip freeze > requirements.txt 

status codes
400 = get request
403 = forhidden
404 = not found
500 = internal server error
200 = successful code
