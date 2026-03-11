from fastapi import FastAPI

from db_main import all_items, add_item, update_item, delete_item, update_delete_item

app = FastAPI()

@app.get('/tasks')
async def item_all():
    result = all_items()
    return result

@app.post('/task_add')
async def item_add(id: int, name: str, source: str):
    result = add_item(id, name, source)
    return result

@app.put('/item_update')
async def item_update(id: int, name: str, source: str):
    result = update_delete_item(id, name, source, method='update')
    return result

@app.delete('/item_delete')
async def item_delete(id: int):
    result = update_delete_item(id, method='delete')
    return result