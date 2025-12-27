from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# -----------------------
# Root Route (Status Check)
# -----------------------
@app.get("/")
def root():
    return {"status": "Todo API is running"}

# -----------------------
# Todo Model (Pydantic)
# -----------------------
class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False

# -----------------------
# Fake In-Memory Database
# -----------------------
todos: List[Todo] = []

# -----------------------
# Create Todo (CREATE)
# -----------------------
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo created successfully", "todo": todo}

# -----------------------
# Read All Todos (READ)
# -----------------------
@app.get("/todos")
def get_todos():
    return todos

# -----------------------
# Read Single Todo (READ)
# -----------------------
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# -----------------------
# Update Todo (UPDATE)
# -----------------------
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {"message": "Todo updated successfully", "todo": updated_todo}
    raise HTTPException(status_code=404, detail="Todo not found")

# -----------------------
# Delete Todo (DELETE)
# -----------------------
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            deleted_todo = todos.pop(index)
            return {"message": "Todo deleted successfully", "todo": deleted_todo}
    raise HTTPException(status_code=404, detail="Todo not found")
