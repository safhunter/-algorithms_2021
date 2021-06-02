"""
Задание 6.
Задание на закрепление навыков работы с очередью

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
from abc import ABC, abstractmethod


class IIterableCollection(ABC):

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def push(self, item):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass


class Task:

    def __init__(self, task_id: int):
        self.task_id = task_id

    def __str__(self):
        return str(self.task_id)


class QueueClass(IIterableCollection):

    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def push(self, item):
        self.elements.insert(0, item)

    def pop(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def __iter__(self):
        return self.elements.__iter__()

    def __str__(self):
        result = '-> '
        for elem in self.elements:
            result = result + f'{elem} '
        result = result + '->'
        return result


class TasksCollection:

    def __init__(self, task_collection: IIterableCollection):
        self.collection = task_collection

    def is_empty(self) -> bool:
        return self.collection.is_empty()

    def push(self, new_task: Task):
        self.collection.push(new_task)

    def pop(self) -> Task:
        if self.collection.is_empty():
            raise IndexError(f'Task collection is empty')
        else:
            return self.collection.pop()

    def size(self):
        return self.collection.size()

    def __str__(self):
        return str(self.collection)


class BaseTasks(TasksCollection):

    def __init__(self, task_collection: IIterableCollection):
        super().__init__(task_collection)

    def __str__(self):
        return 'Base tasks:\n' + super().__str__()


class ActiveTasks(TasksCollection):

    def __init__(self, task_collection: IIterableCollection):
        super().__init__(task_collection)

    def __str__(self):
        return 'Active tasks:\n' + super().__str__()


class CompletedTasks(TasksCollection):

    def __init__(self, task_collection: IIterableCollection):
        super().__init__(task_collection)

    def __str__(self):
        return 'Completed tasks:\n' + super().__str__()


class RevisionTasks(TasksCollection):

    def __init__(self, task_collection: IIterableCollection):
        super().__init__(task_collection)

    def __str__(self):
        return 'Revision tasks:\n' + super().__str__()


base_desk = BaseTasks(QueueClass())
active_desk = ActiveTasks(QueueClass())
completed_desk = CompletedTasks(QueueClass())
revision_desk = RevisionTasks(QueueClass())
[base_desk.push(Task(x)) for x in range(20)]

print(base_desk)
print(active_desk)
print(completed_desk)
print(revision_desk)

for i in range(10):
    active_desk.push(base_desk.pop())

print(base_desk)
print(active_desk)
print(completed_desk)
print(revision_desk)

for i in range(5):
    completed_desk.push(active_desk.pop())

print(base_desk)
print(active_desk)
print(completed_desk)
print(revision_desk)

for i in range(2):
    revision_desk.push(completed_desk.pop())

print(base_desk)
print(active_desk)
print(completed_desk)
print(revision_desk)
