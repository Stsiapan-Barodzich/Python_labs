from fastapi import FastAPI
from routers import tasks

app = FastAPI(title="Task Manager API")
app.include_router(tasks.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to Task Manager API!"}