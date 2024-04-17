document.addEventListener('DOMContentLoaded', function() {
    const taskInput = document.getElementById('taskInput');
    const addTaskBtn = document.getElementById('addTaskBtn');
    const taskList = document.getElementById('taskList');
    const statusCount = document.getElementById('statusCount');
    let completedTasks = 0;
  
    addTaskBtn.addEventListener('click', function() {
      if (taskInput.value !== '') {
        const newTask = document.createElement('li');
        newTask.innerHTML = `
          <span>${taskInput.value}</span>
          <button class="taskDoneBtn">✓</button>
          <span class="deleteTaskBtn">🗑</span>
        `;
        taskList.appendChild(newTask);
        taskInput.value = '';
      }
    });
  
    taskList.addEventListener('click', function(e) {
      if (e.target.classList.contains('taskDoneBtn')) {
        const task = e.target.parentElement;
        task.classList.toggle('taskDone');
        if (task.classList.contains('taskDone')) {
          completedTasks++;
        } else {
          completedTasks--;
        }
        statusCount.textContent = `Tasks completed: ${completedTasks}`;
      }
  
      if (e.target.classList.contains('deleteTaskBtn')) {
        const task = e.target.parentElement;
        task.remove();
      }
    });
  });
  