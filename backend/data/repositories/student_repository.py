from backend.data.repositories.course_repository import CourseRepository
from backend.data.repositories.user_repository import UserRepository


class StudentRepository(UserRepository):
    def __init__(self):
        self.course_repository = CourseRepository()

    def view_available_courses(self) -> list:
        courses = self.course_repository.available_courses()
        return courses


    def get_course_by_id(self,course_id):
        return self.course_repository.get_course_by_id(course_id)




