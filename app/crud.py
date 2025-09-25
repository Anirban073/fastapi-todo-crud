from database import SessionLocal
from models import Todo
from sqlalchemy import select, update, delete

# ----------------------------
# CREATE
# ----------------------------
def create_todo(title: str, description: str = None):
    with SessionLocal() as session:
        todo = Todo(title=title, description=description)
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return todo

# ----------------------------
# READ ALL
# ----------------------------
def get_todos():
    with SessionLocal() as session:
        stmt = select(Todo)
        todo = session.scalars(stmt).all()
        return todo

# ----------------------------
# READ BY ID
# ----------------------------
def get_todo(todo_id: int):
    with SessionLocal() as session:
        # todo = select(Todo).where(Todo.id == todo_id)
        todo = session.get(Todo, todo_id)
        return todo

# ----------------------------
# UPDATE
# ----------------------------
def update_todo(todo_id: int, title: str = None, description: str = None, completed: bool = None):
    with SessionLocal() as session:
        todo = session.get(Todo, todo_id)
        if not todo:
            return None
        if title is not None:
            todo.title = title
        if description is not None:
            todo.description = description
        if completed is not None:
            todo.completed = completed
        session.commit()
        session.refresh(todo)
        return todo

# ----------------------------
# DELETE
# ----------------------------
def delete_todo(todo_id: int):
    with SessionLocal() as session:
        # todo = select(Todo).where(Todo.id == todo_id)
        todo = session.get(Todo, todo_id)
        if not todo:
            return False
        session.delete(todo)
        session.commit()
        return True
    
