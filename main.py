class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age 
    
    def get_age(self):
        return self.age 
    
    def get_name(self):
        return self.name
    
    def get_info(self):
        return self.name, self.age
    

Vasya=Person("Иванов Василий Викторович",11)
# print(Vasya.get_age())
# print(Vasya.get_name())
# print(Vasya.get_info())


class Student(Person):
    def __init__(self, name: str, age: int, grade: int, subjects: list) -> None:
        super().__init__(name, age)
        self.__grade = grade
        self.subjects = subjects

    def get_info(self):
        return super().get_info(), self.__grade, self.subjects
        
    def get_grade(self):
        return self.__grade
    
    def finish_grade(self):
        return self.__grade + 1 
    

asya=Student("Иванов Василий Викторович", 11, 3, ["maths","physics"])
# print(asya.get_info())
# print(asya.get_grade())
# print(asya.finish_grade())

class Worker:
    def __init__(self, position: str, wage: int) -> None:
        self.position = position
        self.wage = wage

    def get_wage(self):
        return self.wage
    
    def get_position(self):
        return self.position
    
class Teacher(Person, Worker):
    def __init__(self, name: str, age: int, position: str, wage: int) -> None:
        Person.__init__(self, name, age)
        Worker.__init__(self, position, wage)

    def get_info(self):
        return self.name, self.age, self.position, self.wage


alera=Teacher("Ярцев Валерий Рустэмович", 20, "Informatics teacher", 200)
print(alera.get_info())

class Group:
    def __init__(self, students: Student, group_teacher: Teacher, group_name: str) -> None:
        self.students = students
        self.group_teacher = group_teacher
        self.group_name = group_name

    def get_info(self):
        return {
            'students' : [student.get_info() for student in self.students],
            'group_teacher' : self.group_teacher.get_info(),
            'group_name': self.group_name
        }
    def get_students_number(self):
        return len(self.students)

students = [   
Student("Виталий",23,3,["Maths","Physcis"]),
Student("Геннадий",21,3,["Maths","Physcis"]),
Student("Иван",43,3,["Maths","Physcis","PE"])
 ]
teacher=Teacher("ЯрцевВалерийРустэмович",20,"Informaticsteacher",200)
group = Group(students, teacher, group_name='Group B')
# print(group.get_info())
# print(group.get_students_number())


from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, age: int, size: int, habitat: str) -> None:
        self.age = age
        self.size = size 
        self.habibtat = habitat


    @abstractmethod
    def make_sound(self):
        pass 


class Dog(Animal):
    def make_sound(self):
        return 'Gav Gav'
    
class Cat(Animal):
    def make_sound(self):
        return 'Myau Myau'

class Dolphin(Animal):
    def make_sound(self):
        return 'Click Click'

class Elephant(Animal):
    def make_sound(self):
        return 'tru-tu-tu'

class CircusAnimalEnsemble:
    def __init__(self, animals=None):
        self.animals = animals if animals is not None else []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def speak(self):
        for animal in self.animals:
            print(animal.make_sound())


dog = Dog(age=3, size="Medium", habitat="House")

cat = Cat(age=2, size="Small", habitat="House") 

dolphin = Dolphin(age=1, size='Big', habitat='House')

elephant = Elephant(age=4, size='Gigantic', habitat='Universe')

circus_ensemble = CircusAnimalEnsemble()
circus_ensemble.add_animal(dog)
circus_ensemble.add_animal(cat)
circus_ensemble.add_animal(dolphin)
circus_ensemble.add_animal(elephant)
print(circus_ensemble.speak())




