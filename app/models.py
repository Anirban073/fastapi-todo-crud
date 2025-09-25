from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean
from database import engine

class Base(DeclarativeBase):
    pass

class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(250), nullable=True)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)


    # def __repr__(self) -> str:
    #     return f"<Todo(id={self.id}, title={self.title}, description={self.description})>"
    


# create table
Base.metadata.create_all(bind=engine)
