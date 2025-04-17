import os

from bson import ObjectId
from flask.cli import load_dotenv
from pymongo import MongoClient

from backend.data.models.course import Course
from backend.excpetions.course_already_exist_error import CourseAlreadyExistError
from backend.excpetions.course_not_found import CourseNotFound
from backend.excpetions.creation_error import CreationError

load_dotenv()
class CourseRepository:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client[os.getenv('DB_NAME')]
        self.collection = self.db[os.getenv('COLLECTION_NAME')]


    def existed_course(self,course:str) -> bool:
        return self.collection.find_one({'course':course}) is not None


    def existed_course(self,course_id:int) -> bool:
        return self.collection.find_one({'course_id':course_id}) is not None

    def create_course(self, course:str) -> None:
        course = course.strip().lower()

        if self.existed_course(course):
            return CourseAlreadyExistError("This course already exists")

        course = Course(course)

        try:
            result = self.collection.insert_one(course.__dict__)
            course = self.get_user_by_id(result.inserted_id)
            return course
        except Exception:
            raise CreationError("Failed to create course")

    def get_course_by_id(self, course_id) -> str:
        course = self.collection.find_one({'_id': ObjectId(course_id)})
        if not course:
            raise CourseNotFound("Course id not found")
        return course["course_name"]


    def available_courses(self) -> list:
        courses = self.collection.find()
        return [
            {
                **course,
                "_id": str(course["_id"])
            }
            for course in courses
        ]


    def get_id_by_course_name(self,course_name):
        course = self.collection.find_one({'course_name':course_name})
        if not course:
            raise CourseNotFound("course not found")
        return str(course["_id"])


    def remove_course(self,course_name:str):
        if self.existed_course(course_name):
            self.collection.delete_one({'course_name':course_name})
        else:
            raise CourseNotFound("Course not found")

    def remove_course(self,course_id:int) -> None:
        if self.existed_course(course_id):
            self.collection.delete_one({'course_id':course_id})
        else:
            raise CourseNotFound("Invalid course id")






