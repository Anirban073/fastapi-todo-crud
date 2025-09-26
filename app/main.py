from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Absolute imports from app/
from app.schemas import TodoCreate, TodoUpdate, TodoResponse
from app.crud import create_todo, get_todos, get_todo, update_todo, delete_todo

app = FastAPI()

# Templates folder is directly under project root
templates = Jinja2Templates(directory="templates")

# ---------------- Routes ---------------- #

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    # Renders templates/index.html
    return templates.TemplateResponse("index.html", {"request": request})

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
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.put("/todos/{todo_id}", response_model=TodoResponse)
def api_update_todo(todo_id: int, todo: TodoUpdate):
    updated = update_todo(
        todo_id,
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated

@app.delete("/todos/{todo_id}")
def api_delete_todo(todo_id: int):
    success = delete_todo(todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}
