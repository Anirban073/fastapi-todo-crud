from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLite database file in project root
DATABASE_URL = "sqlite:///./sqlite.db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
