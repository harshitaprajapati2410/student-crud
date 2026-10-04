from fastapi import FastAPI
from routers.student_routes import srouter

app = FastAPI()

app.include_router(srouter)