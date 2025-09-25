const API_URL = "http://127.0.0.1:8000/todos/";

const todoForm = document.getElementById("todoForm");
const todoList = document.getElementById("todoList");

// Fetch and render todos
async function fetchTodos() {
  const res = await fetch(API_URL);
  const todos = await res.json();

  todoList.innerHTML = "";
  todos.forEach(todo => {
    const li = document.createElement("li");
    li.innerHTML = `
      <span>
        <strong>${todo.title}</strong> - ${todo.description || ""}
        ${todo.completed ? "✔️" : ""}
      </span>
      <span>
        <button class="action complete" onclick="toggleComplete(${todo.id}, ${todo.completed})">✔️</button>
        <button class="action edit" onclick="editTodo(${todo.id})">✏️</button>
        <button class="action delete" onclick="deleteTodo(${todo.id})">🗑️</button>
      </span>
    `;
    todoList.appendChild(li);
  });
}

// Add todo
todoForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const title = document.getElementById("title").value;
  const description = document.getElementById("description").value;

  await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, description })
  });

  todoForm.reset();
  fetchTodos();
});

// Delete todo
async function deleteTodo(id) {
  await fetch(API_URL + id, { method: "DELETE" });
  fetchTodos();
}

// Toggle complete
async function toggleComplete(id, completed) {
  await fetch(API_URL + id, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ completed: !completed })
  });
  fetchTodos();
}

// Edit todo (simple prompt)
async function editTodo(id) {
  const newTitle = prompt("Enter new title:");
  const newDescription = prompt("Enter new description:");

  if (newTitle !== null && newDescription !== null) {
    await fetch(API_URL + id, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        title: newTitle,
        description: newDescription
      })
    });
    fetchTodos();
  }
}

// Load todos on page load
fetchTodos();
