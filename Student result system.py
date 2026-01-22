class StudentResultSystem:
    def __init__(self, student_name, matric_number, score):
        self.student_name = student_name
        self.matric_number = matric_number
        self.score = score
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.score >= 70:
            return "A"
        elif self.score >= 60:
            return "B"
        elif self.score >= 50:
            return "C"
        elif self.score >= 45:
            return "D"
        else:
            return "F"

    def display_result(self):
        print("Student Result")
        print("Name:", self.student_name)
        print("Matric Number:", self.matric_number)
        print("Score:", self.score)
        print("Grade:", self.grade)


# Program Execution
student = StudentResultSystem("David", "23467", 75)
student.display_result()
