# 4, 5, 6
# Создать API для обновления информации о пользователе в базе данных.
# Приложение должно иметь возможность принимать PUT, DELETE запросы с данными
# пользователей и обновлять их в базе данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для обновления информации о пользователе (метод PUT, DELETE ).
# Реализуйте валидацию данных запроса и ответа
# Приложение должно использовать шаблонизатор Jinja для динамического формирования HTML
# страницы.
# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja

import pydantic
import uvicorn
from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory='./templates')

users = []


class User(BaseModel):
    id_: int
    name: str
    email: pydantic.EmailStr
    password: pydantic.SecretStr


@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get('/form/')
async def add_user_form(request: Request):
    return templates.TemplateResponse('form.html', {'request': request})


@app.get('/users/')
async def all_users():
    return {'users': users}


@app.post('/users/add')
async def add_users(user: User):
    users.append(user)
    return {"user": user, "status": "added"}


@app.post('/user/add')
async def add_user(id_=Form(), name=Form(), email=Form(), password=Form()):
    users.append(User(id_=id_, name=name, email=email, password=password))
    return RedirectResponse('/', status_code=302)


@app.put('/users/update/{user_id}')
async def update_user(user_id: int, up_user: User):
    for user in users:
        if user.id_ == user_id:
            user.id_ = up_user.id_
            user.name = up_user.name
            user.email = up_user.email
            user.password = up_user.password
            return {"user": user, "status": "updated"}
    return HTTPException(404, 'User not found')


@app.delete('/users/delete/{user_id}')
async def delete(user_id: int):
    for user in users:
        if user.id_ == user_id:
            users.remove(user)
            return {"status": "success"}
    return HTTPException(404, 'User not found')


if __name__ == "__main__":
    uvicorn.run("task_1:app", port=8000)

