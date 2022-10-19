const options = {};
const itemTask = 'task';
const modalElement = document.getElementById('taskModal');
const modalOpenElement = document.getElementsByName('task-open-btn');
const modalCloseElement = document.getElementById('task-close-btn');
const modalUpdateElement = document.getElementById('task-update-btn');
const modalInputElement = document.getElementById('recipient-name');
const modalTextareaElement = document.getElementById('message-text');
const modal = new bootstrap.Modal(modalElement, options);
let task_id = '';

const getTaskData = async(id) => {
    try {
        const response = await fetch(`/task/update-task/${id}`);
        const task = await response.json();
        return task;
    } catch (error) {
        alert('Не удалось загрузить данные');
    }
};

const updateTask = async(task) => {
    try {
        await fetch('/task/process-update-task', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            body: JSON.stringify(task)
        });
    } catch (error) {
        alert('Не удалось отправить данные');
    }
};

for (let i = 0; i < modalOpenElement.length; i++) {
    modalOpenElement[i].addEventListener('click', async() => {
        task_id = modalOpenElement[i].id
        const task = await getTaskData(modalOpenElement[i].id);
        if (task) {
            modalInputElement.value = task.title;
            modalTextareaElement.value = task.text;
        }
        modal.show();
    });
};

modalCloseElement.addEventListener('click', () => {
    modal.hide();
});

modalUpdateElement.addEventListener('click', async() => {
    const text = modalTextareaElement.value;
    const title = modalInputElement.value;
    const task = await getTaskData(task_id);
    const data = {
        id: task.id,
        title,
        text
    };
    await updateTask(data);
    window.location.reload();
});