import json


TASKS_FILE_PATH = 'tasks.json'
ENCODING = 'utf-8'


def all_tasks():
    """Получить все задачи"""
    with open(TASKS_FILE_PATH, 'r', encoding=ENCODING) as f:
        return json.load(f)


def get_completed_tasks():
    """Получить выполненные задачи"""
    tasks = all_tasks()
    return [task for task in tasks if task.get('completed') == True]


def get_pending_tasks():
    """Получить невыполненные задачи"""
    tasks = all_tasks()
    return [task for task in tasks if task.get('completed') == False]
    
    
def add_task(task_id, title, description='', completed=False):
    """Добавить новую задачу"""
    tasks = all_tasks()
    
    if any(task.get('id') == task_id for task in tasks):
        return {'message': 'Задача с таким ID уже существует', 'error': True}
    
    new_task = {
        "id": task_id,
        "title": title,
        "description": description,
        "completed": completed,
        "notes": ""
    }
    tasks.append(new_task)
    
    with open(TASKS_FILE_PATH, 'w', encoding=ENCODING) as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)
    
    return {'message': 'Задача добавлена'}


def delete_task(task_id):
    """Удалить задачу"""
    tasks = all_tasks()
    new_tasks = [task for task in tasks if task.get('id') != task_id]
    
    if len(new_tasks) == len(tasks):
        return {'message': 'Задача не найдена'}
    
    with open(TASKS_FILE_PATH, 'w', encoding=ENCODING) as f:
        json.dump(new_tasks, f, ensure_ascii=False, indent=4)
    
    return {'message': 'Задача удалена'}


def update_task(task_id, title=None, description=None, completed=None, notes=None):
    """Обновить задачу"""
    tasks = all_tasks()
    
    for task in tasks:
        if task.get('id') == task_id:
            if title is not None:
                task['title'] = title
            if description is not None:
                task['description'] = description
            if completed is not None:
                task['completed'] = completed
            if notes is not None:
                task['notes'] = notes
            
            with open(TASKS_FILE_PATH, 'w', encoding=ENCODING) as f:
                json.dump(tasks, f, ensure_ascii=False, indent=4)
            return {'message': 'Задача обновлена'}
    
    return {'message': 'Задача не найдена'}

    
    
    