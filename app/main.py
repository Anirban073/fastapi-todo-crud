from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

# Import schemas and crud functions
from schemas import TodoCreate, TodoUpdate, TodoResponse
from crud import create_todo, get_todos, get_todo, update_todo, delete_todo

app = FastAPI()

# --- Correct static and template paths ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "templates")),
    name="static"
)

# ---------------------------
# Home route (Frontend)
# ---------------------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# ---------------------------
# CRUD API routes
# ---------------------------

# Create
@app.post("/todos/", response_model=TodoResponse)
def api_create_todo(todo: TodoCreate):
    return create_todo(todo.title, todo.description)

# Read all
@app.get("/todos/", response_model=list[TodoResponse])
def api_get_todos():
    return get_todos()

# Read by id
@app.get("/todos/{todo_id}", response_model=TodoResponse)
def api_get_todo(todo_id: int):
    todo = get_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="todo not found")
    return todo

# Update
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

# Delete
@app.delete("/todos/{todo_id}")
def api_delete_todo(todo_id: int):
    success = delete_todo(todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="todo not found")
    return {"message": "todo deleted successfully"}
