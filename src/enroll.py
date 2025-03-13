import os
from course import Course

class Enrollment:
    def __init__(self):
        self.course = Course()
        self.__enrolled_courses = {}
        self.ensure_file_exists()
        self.load_enrolled_courses()

    def ensure_file_exists(self):
        if not os.path.exists("enrolled_courses.txt"):
            with open("enrolled_courses.txt", "w") as file:
                pass

    def enroll(self, student_email, course_name):
        available_courses = self.course.view_course()
        if course_name not in available_courses:
            raise ValueError(f"Course '{course_name}' does not exist.")

        if student_email in self.__enrolled_courses.keys():
            if self.__enrolled_courses[student_email] == course_name:
                raise ValueError(f"You are already enrolled in '{course_name}'.")
        else:
            self.__enrolled_courses[student_email] = course_name
            print(f"You have successfully enrolled in {course_name}.")
            self.save_enrolled_courses()

    def un_enroll(self, student_email, course_name):
        if student_email in self.__enrolled_courses and self.__enrolled_courses[student_email] == course_name:
            del self.__enrolled_courses[student_email]
            print(f"You have successfully Un enrolled from '{course_name}'.")
            self.save_enrolled_courses()
        else:
            raise ValueError(f"You are  not enrolled in '{course_name}'.")

    def save_enrolled_courses(self):
        with open("enrolled_courses.txt", "w") as file:
            for student_email, course_name in self.__enrolled_courses.items():
                file.write(f"{student_email}:{course_name}\n")

    def load_enrolled_courses(self):
        try:
            with open("enrolled_courses.txt", "r") as file:
                for line in file:
                    student_email, course_name = line.strip().split(":")
                    self.__enrolled_courses[student_email] = course_name
        except Exception as e:
            print(f"Error loading enrollments: {e}")

    def view_enrollments(self):
        enrolled_students = []
        if not self.__enrolled_courses:
            print("No enrollments found.")
        else:
            for student_email in self.__enrolled_courses:
                enrolled_students.append(student_email)
        return enrolled_students

    def view_students_in_course(self, course_name):
        students = [student_email for student_email, cn in self.__enrolled_courses.items() if cn == course_name]
        if students:
            print(f"Students enrolled in '{course_name}':")
            for student_email in students:
                print(f"- {student_email}")
        else:
            print(f"No students enrolled in '{course_name}'.")

    def view_enrolled_courses(self):
        enrolled_courses = list((self.__enrolled_courses.values()))
        return enrolled_courses