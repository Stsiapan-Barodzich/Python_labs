class Student:
    # Атрибут класса для подсчёта количества студентов
    students_quantity = 0

    def __init__(self, name, course, grades):
        self.name = name
        self.course = course
        self.grades = grades
        Student.students_quantity += 1

    def is_honors_student(self):
        """
        Проверяет, является ли студент отличником (средний балл по всем предметам > 8.5)
        """
        total_score = sum(sum(scores) for scores in self.grades.values())
        total_count = sum(len(scores) for scores in self.grades.values())
        return (total_score / total_count) > 8.5

    def avg_score_by_subject(self, subject):
        """
        Возвращает средний балл по заданному предмету
        """
        if subject in self.grades:
            return sum(self.grades[subject]) / len(self.grades[subject])
        else:
            raise ValueError(f"Предмет '{subject}' не найден у студента {self.name}.")

# Пример использования
if __name__ == "__main__":
    student = Student("Anna", 2, {
        "programming": [9, 8, 10, 9, 10],
        "FE": [9, 8, 10, 9, 8]
    })

    print(student.is_honors_student())  # True
    print(f"Average score for programming = {student.avg_score_by_subject('programming')}")
