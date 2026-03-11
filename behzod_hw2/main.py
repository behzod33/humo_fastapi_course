from fastapi import FastAPI

from db_main import (
    all_tasks, 
    get_completed_tasks, 
    get_pending_tasks, 
    add_task, 
    update_task, 
    delete_task
)

app = FastAPI()

@app.get('/tasks')
async def get_all_tasks():
    """Получить все задачи"""
    result = all_tasks()
    return result

@app.get('/tasks/completed')
async def get_completed():
    """Получить все выполненные задачи"""
    result = get_completed_tasks()
    return result

@app.get('/tasks/pending')
async def get_pending():
    """Получить все невыполненные задачи"""
    result = get_pending_tasks()
    return result

@app.post('/tasks')
async def create_task(
        id: int, 
        title: str, 
        description: str = '', 
        completed: bool = False
    ):
    """Создать новую задачу"""
    result = add_task(id, title, description, completed)
    return result

@app.put('/tasks/{task_id}')
async def edit_task(
        task_id: int, 
        title: str = None, 
        description: str = None, 
        completed: bool = None, 
        notes: str = None
    ):
    """Редактировать задачу (менять название, описание, статус, добавлять пометки)"""
    result = update_task(task_id, title, description, completed, notes)
    return result

@app.delete('/tasks/{task_id}')
async def remove_task(task_id: int):
    """Удалить задачу"""
    result = delete_task(task_id)
    return result