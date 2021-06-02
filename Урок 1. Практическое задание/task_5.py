"""
Задание 5.
Задание на закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


class Plate(object):

    def __init__(self, plate_id):
        self.plate_id = plate_id

    def __str__(self):
        return str(self.plate_id)


class PlatesStack(object):

    def __init__(self, plates_per_stack: int):
        if plates_per_stack == 0:
            raise ValueError('Stack max count must be grater then 0')
        self.plates_per_stack = plates_per_stack
        self.stack = []

    def put_plate(self, new_plate: Plate):
        if not self.is_full():
            self.stack.append(new_plate)

    def get_plate(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_full(self):
        return len(self.stack) >= self.plates_per_stack

    def is_empty(self):
        return self.stack == []


class Plates(object):

    def __init__(self, plates_per_stack: int):
        if plates_per_stack == 0:
            raise ValueError('Stack max count must be grater then 0')
        self.plates_per_stack = plates_per_stack
        self.stacks_list = []
        self.stacks_list.append(PlatesStack(plates_per_stack))

    def put_plate(self, new_plate: Plate):
        if self.stacks_list[len(self.stacks_list)-1].is_full():
            print(f'Add new plates stack')
            self.stacks_list.append(PlatesStack(self.plates_per_stack))
        self.stacks_list[len(self.stacks_list) - 1].put_plate(new_plate)

    def get_plate(self):
        if self.have_plates():
            taken_plate = self.stacks_list[len(self.stacks_list) - 1].get_plate()
            if self.stacks_list[len(self.stacks_list)-1].is_empty():
                print(f'Remove plates stack')
                self.stacks_list.pop()
            return taken_plate
        else:
            return None

    def have_plates(self):
        return len(self.stacks_list) > 0


plates_list = [Plate(x) for x in range(100)]
plates = Plates(3)
for plate in plates_list:
    plates.put_plate(plate)

while plates.have_plates():
    print(f'Take plate: {plates.get_plate()}')

