async function fetchTodos(){
    const URL="http://localhost:5001/api/todos";
    const settings = {
        method : "GET"
    }
    // const response = await fetch( URL, settings);
    // const data = await response.json();
    // console.log(data);

    fetch(URL, settings)
        .then(response => response.json() )
        .then(function(data) {
            const results = document.querySelector('.results');
            results.innerHTML = "";

            for (todo of data) {
                results.innerHTML += `
                <div class="todo">
                    <h3>Description: ${todo.description}</h3>
                    <h5>Status: ${todo.status}</h5>
                    <button type="submit" onclick="deleteTodo(${todo.id})">Delete</button>
                </div>
                `
            }
            results.innerHTML += `<button type="submit" onclick="collapseTodos()">Collapse Todos</button>`;
        })
}

function collapseTodos(){
    const results = document.querySelector('.results');
    results.innerHTML = 'Click button to retrieve all ToDos';
}

async function deleteTodo(id) {
    const URL = `http://localhost:5001/api/delete/todo/${id}`;
    const settings = {
        method: "DELETE"
    }
    const response = await fetch(URL, settings)
    console.log(response);
    fetchTodos();
}

async function addTodo(event) {
    event.preventDefault();

    const data = {
        "description": document.querySelector('#description').value,
        "status": document.querySelector('#status').value,
        "user_id": 1  // would want to dynamically assign based on logged in users id
    }

    const URL = "http://localhost:5001/api/add/todo";
    const settings = {
        method:"POST",
        headers: {
            "Content-type" : "application/json",
        },
        body:JSON.stringify(data)
    }

    const response = await fetch(URL, settings);
    const jsonData = await response.json();
    console.log(jsonData);
    fetchTodos();
}
