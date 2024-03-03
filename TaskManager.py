from typing import List


class Task:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description


class TaskManager:

    def __init__(self):
        self.__tasks = []

    def add_task(self, title: str, description: str):
        task = Task(title, description)
        self.__tasks.append(task)

    @property
    def tasks(self):
        return self.__tasks


if __name__ == "__main__":
    # Создаем объект TaskManager
    task_manager = TaskManager()

    # Добавляем задачи
    task_manager.add_task("Домашка", "Сделать домашку")
    task_manager.add_task("Спросить у училки", "Сделала ли она домашку от тайлера")

    # Получаем и выводим список задач
    tasks = task_manager.tasks
    for idx, task in enumerate(tasks, start=1):
        print(f"Задача {idx}: {task.title} - {task.description}")