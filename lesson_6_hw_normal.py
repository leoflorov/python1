# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики. У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя, один учитель может преподавать в неограниченном кол-ве классов
# свой определенный предмет. Т.е. Учитель Иванов может преподавать математику у 5А и 6Б, но больше математику не
# может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Person:
    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        # self.age = age
        # self.classroom = classroom

    def get_full_name(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname

    def get_short_name(self):
        return f"{self.surname.title()}, {self.name[0].upper()}, {self.patronymic[0].upper()}"


if __name__ == '__main__':  # Тестирование.
    people1 = Person('Иван', 'Иванович', 'Иванов')
    print(people1.get_full_name())
    print(people1.get_short_name())


class Student(Person):
    def __init__(self, name, patronymic, surname, mother, father, school_class):
        super().__init__(name, surname, patronymic)
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.mother = mother
        self.father = father
        self.school_class = school_class

#     def all_classes(self):
#         pass
#
#
# if __name__ == '__main__':  # Тестирование.
#     st_1 = Student('Семен', 'Семенович', 'Семенов', 'Анна Михайлова', 'Алексанр Семенов', '7а')
#     st_2 = Student('Сергей', 'Сергеевич', 'Сергеев', 'Ольга Сергеева', 'Андрей Сергеев', '7б')
#     st_3 = Student('Олег', 'Олегович', 'Петров', 'Юлия Петрова', 'Олег Петров', '7а')
#     print(Student.all_classes(st_1))


class Teacher(Person):
    def __init__(self, name, patronymic, surname, subject):
        Person.__init__(self, name, patronymic, surname)
        self.subject = subject


class ClassRooms:
    def __init__(self, class_room, teachers):
        self.class_room = class_room
        self.teachersdict = {t.subject: t for t in teachers}


if __name__ == '__main__':  # Тестирование.
    teachers = [Teacher('Иван', 'Иванович', 'Иванов', 'Математика'),
                Teacher('Петр', 'Петрович', 'Петров', 'Литература'),
                Teacher('Сидор', 'Сидорович', 'Сидоров', 'Физика'),
                Teacher('Дмитрий', 'Дмитриевич', 'Дмитриев', 'История'),
                Teacher('Никита', 'Никитиевич', 'Никишин', 'Биология')]
    classes = [ClassRooms('11 А', [teachers[0], teachers[1], teachers[2]]),
               ClassRooms('11 Б', [teachers[1], teachers[3], teachers[4]]),
               ClassRooms('10 А', [teachers[3], teachers[1], teachers[0]])]
    parents = [Person('Семен', 'Семенович', 'Семенов'),
               Person('Светлана', 'Савельевна', 'Семенова'),
               Person('Роман', 'Романович', 'Романов'),
               Person('Римма', 'Романовна', 'Романова'),
               Person('Сергей', 'Сергеевич', 'Сергеев'),
               Person('Юлия', 'Викторвна', 'Сергеева')]
    students = [Student('Игорь', 'Cеменович', 'Семенов', parents[0], parents[1], classes[0]),
                Student('Ольга', 'Романова', 'Романова', parents[2], parents[3], classes[1]),
                Student('Александр', 'Сергеевич', 'Сергеев', parents[4], parents[5], classes[2])]
    print('Список классов в школе: ')

    for f in classes:
        print(f.class_room)

    for f in classes:
        print('Учителя, преподающие в {} классе:'.format(f.class_room))
        for teacher in classes[0].teachersdict.values():
            print(teacher.get_full_name())
    for f in classes:
        print("Ученики в классе {}:".format(f.class_room))
        for st in students:
            print(st.get_short_name())

    for f in students:
        print('Список предметов ученика {}'.format(f.school_class))
        for teacher in classes[0].teachersdict.values():
            print(teacher.get_full_name())
