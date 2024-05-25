document.addEventListener('DOMContentLoaded', () => {
    const taskForm = document.getElementById('task-form');
    const taskInput = document.getElementById('task-input');
    const taskList = document.getElementById('task-list');

    taskForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const task = taskInput.value.trim();
        if (task) {
            fetch('/add', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ task }),
            })
            .then(response => response.json())
            .then(data => {
                const li = document.createElement('li');
                li.className = 'list-group-item d-flex justify-content-between align-items-center';
                li.dataset.id = data.id;
                li.innerHTML = `
                    <span class="task-text">${data.task}</span>
                    <div>
                        <button class="btn btn-secondary btn-sm edit-btn mr-2">Edit</button>
                        <button class="btn btn-danger btn-sm delete-btn">Delete</button>
                    </div>
                `;
                taskList.appendChild(li);
                taskInput.value = '';
            })
            .catch(error => console.error('Error:', error));
        }
    });

    taskList.addEventListener('click', (e) => {
        if (e.target.classList.contains('delete-btn')) {
            const taskId = e.target.closest('li').dataset.id;
            fetch(`/delete/${taskId}`, {
                method: 'DELETE',
            })
            .then(response => response.json())
            .then(() => {
                e.target.closest('li').remove();
            })
            .catch(error => console.error('Error:', error));
        }

        if (e.target.classList.contains('edit-btn')) {
            const taskElement = e.target.closest('li');
            const taskId = taskElement.dataset.id;
            const taskText = taskElement.querySelector('.task-text');
            const newTask = prompt('Edit Task', taskText.textContent);
            if (newTask) {
                fetch(`/edit/${taskId}`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ task: newTask }),
                })
                .then(response => response.json())
                .then(data => {
                    taskText.textContent = data.task;
                })
                .catch(error => console.error('Error:', error));
            }
        }
    });
});