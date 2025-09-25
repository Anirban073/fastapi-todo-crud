from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

# Relative imports
from .schemas import TodoCreate, TodoUpdate, TodoResponse
from .crud import create_todo, get_todos, get_todo, update_todo, delete_todo

app = FastAPI()

# Correct static and template paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # points to app/
PROJECT_ROOT = os.path.join(BASE_DIR, "..")           # project root

templates = Jinja2Templates(directory=os.path.join(PROJECT_ROOT, "templates"))

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(PROJECT_ROOT, "templates")),
    name="static"
)

# Home route
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# CRUD API routes

@app.post("/todos/", response_model=TodoResponse)
def api_create_todo(todo: TodoCreate):
    return create_todo(todo.title, todo.description)

@app.get("/todos/", response_model=list[TodoResponse])
def api_get_todos():
    return get_todos()

@app.get("/todos/{todo_id}", response_model=TodoResponse)
def api_get_todo(todo_id: int):
    todo = get_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="todo not found")
    return todo

@app.put("/todos/{todo_id}", response_model=TodoResponse)
def api_update_todo(todo_id: int, todo: TodoUpdate):
    updated = update_todo(
        todo_id,
        title=todo.title,
        description=todo.description,
        completed=todo.completed
    )
    if not updated:
        raise HTTPException(status_code=404, detail="todo not found")
    return updated

@app.delete("/todos/{todo_id}")
def api_delete_todo(todo_id: int):
    success = delete_todo(todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="todo not found")
    return {"message": "todo deleted successfully"}
