from fastapi import FastAPI

app = FastAPI(title='My App', version='0.1')

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get('/get_params/')
async def get_params(name: str, age: int):
    return {
        'result': 'OK', 
        'name': name, 
        'age': age
    }
    
def get_params_func(name, age):
    if isinstance(name, str) and isinstance(age, int):
        return {'result': 'OK'}
    return { 
        'result': 'Валидация не пройдена' 
    }

