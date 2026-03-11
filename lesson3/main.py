from fastapi import FastAPI, Depends
from fastapi.openapi.docs import get_swagger_ui_html
from db import users_all, add_user, update_user, delete_param
from model import AddUser, UpdateUser
from fastapi import status


app = FastAPI(
    title='My App',
    version='1.0'
)

@app.get('/all_user')
async def get_all_users(active: bool):
    result = users_all(active)
    return result


@app.post('/add_user')
async def create_user(input_data: AddUser = Depends()):
    add_user(input_data)
    return {"message": "User created successfully"}


@app.put('/update_user')
async def edit_or_delete_user(input_data: UpdateUser = Depends()):
    delete_param(input_data.id, input_data.param_to_delete)
    return {"message": f"Parameter '{input_data.param_to_delete}' deleted successfully"}


@app.put('/delete_user')
async def delete_user(input_data: UpdateUser = Depends()):
    delete_param(input_data.id, input_data.param_to_delete)
    return {"message": f"Parameter '{input_data.param_to_delete}' deleted successfully"}