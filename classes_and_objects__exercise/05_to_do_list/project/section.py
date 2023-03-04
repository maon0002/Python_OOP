from typing import List

from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task) -> str:

        try:
            task = next(filter(lambda t: t.name == new_task, self.tasks))
        except StopIteration:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str) -> str:

        try:
            task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self) -> str:
        amount_of_completed_tasks = len([x for x in self.tasks if x.completed])
        self.tasks = [x for x in self.tasks if not x.completed]
        return f"Cleared {amount_of_completed_tasks} tasks."

    def view_section(self) -> str:
        output = [f"Section {self.name}:"]
        [output.append(f"{t.details()}") for t in self.tasks]
        return "\n".join(output)


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())

