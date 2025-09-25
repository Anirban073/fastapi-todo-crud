# FastAPI Todo CRUD App 📝

A simple CRUD application built with FastAPI + SQLite.  
Includes both backend APIs and a small frontend (HTML, CSS, JS).

## 🚀 Features
- Create, Read, Update, Delete Todos
- SQLite database
- Frontend with templates (HTML, CSS, JavaScript)
- FastAPI backend

## 📂 Project Structure
project2/
│── app/
│ ├── main.py     # FastAPI entrypoint
│ ├── crud.py     # Database operations
│ ├── database.py # DB connection
│ ├── models.py   # SQLAlchemy models
│ ├── schemas.py  # Pydantic schemas
│── templates/    # Frontend files
│ ├── index.html
│ ├── script.js
│ ├── style.css
│── requirements.txt # Dependencies
│── README.md
│── .gitignore


## ⚡ Run Locally
```bash
# 1. Create virtual environment
python -m venv venv
venv\Scripts\activate   # for Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run server
cd app
uvicorn main:app --reload
