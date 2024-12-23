from fastapi import APIRouter, HTTPException, Query, BackgroundTasks
from schemas import Task
from utils.email import send_email


router = APIRouter(prefix="/tasks", tags=["Tasks"])
tasks = []


@router.post("/", response_model=Task)
def create_task(task: Task, background_tasks: BackgroundTasks):
    if any(task["id"] == task.id for task in tasks):
        raise HTTPException(status_code=400, detail="Задача с таким номером уже существует")
    tasks.append(task.dict())
    background_tasks.add_task(send_email, task.title)
    return task


@router.get("/", response_model=list[Task])
def get_tasks(
    completed: bool = Query(None, description="Фильтр по статусу выполнения"),
    limit: int = Query(None, description="Ограничение на количество задач"),
):
    filtered_tasks = tasks
    if completed is not None:
        filtered_tasks = [task for task in tasks if task["completed"] == completed]
    if limit is not None:
        filtered_tasks = filtered_tasks[:limit]
    return filtered_tasks


@router.put("/{task_id}", response_model=Task)
def update_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            task.update(task.dict())
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")