window.addEventListener("load", () => {
  tasks = JSON.parse(localStorage.getItem("tasks")) || [];
  const nameInput = document.querySelector("#name");

  const newTaskForm = document.querySelector("#newTaskForm");

  const username = localStorage.getItem("username") || "";

  nameInput.value = username;

  nameInput.addEventListener("change", (e) => {
    localStorage.setItem("username", e.target.value);
  });

  newTaskForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const task = {
      newTask: e.target.elements.newTask.value,
      course: e.target.elements.course.value,
      done: false,
      createdAt: new Date().getTime(),
    };
    tasks.push(task);
    localStorage.setItem("tasks", JSON.stringify(tasks));

    e.target.reset();

    DisplayTasks();
  });
});

function DisplayTasks() {
  const taskList = document.querySelector("#taskList");
  taskList.innerHTML = "";

  tasks.forEach((task) => {
    const listItem = document.createElement("div");
    listItem.classList.add("listItem");

    const label = document.createElement("label");
    const input = document.createElement("input");
    const span = document.createElement("span");
    const newTask = document.createElement("div");
    const actions = document.createElement("div");
    const edit = document.createElement("button");
    const deleteButton = document.createElement("button");

    input.type = "checkbox";
    input.checked = task.done;
    span.classList.add("optionCard");

    if (task.course == "course1") {
      span.classList.add("course1");
    } else if (task.course == "course2") {
      span.classList.add("course2");
    } else if (task.course == "course3") {
      span.classList.add("course3");
    } else if (task.course == "course4") {
      span.classList.add("course4");
    } else if (task.course == "course5") {
      span.classList.add("course5");
    } else {
      span.classList.add("course6");
    }

    newTask.classList.add("listContent");
    actions.classList.add("actions");
    edit.classList.add("edit");
    deleteButton.classList.add("delete");

    newTask.innerHTML = `<input type="text" value="${task.newTask}" 
    readonly>`;

    edit.innerHTML = "Edit";
    deleteButton.innerHTML = "Delete";

    label.appendChild(input);
    label.appendChild(span);
    actions.appendChild(edit);
    actions.appendChild(deleteButton);
    listItem.appendChild(label);
    listItem.appendChild(newTask);
    listItem.appendChild(actions);

    taskList.appendChild(listItem);

    if (task.done) {
      listItem.classList.add("done");
    }

    input.addEventListener("click", (e) => {
      task.done = e.target.checked;
      localStorage.setItem("tasks", JSON.stringify(tasks));

      if (task.done) {
        listItem.classList.add("done");
      } else {
        listItem.classList.remove("done");
      }
      DisplayTasks();
    });

    edit.addEventListener("click", (e) => {
      const input = newTask.querySelector("input");
      input.removeAttribute("readonly");
      input.focus();
      input.addEventListener("blur", (e) => {
        input.setAttribute("readonly", true);
        task.newTask = e.target.value;
        localStorage.setItem("tasks", JSON.stringify(tasks));
        DisplayTasks();
      });
    });

    deleteButton.addEventListener("click", (e) => {
      tasks = tasks.filter((t) => t != task);
      localStorage.setItem("tasks", JSON.stringify(tasks));
      DisplayTasks();
    });
  });
}
