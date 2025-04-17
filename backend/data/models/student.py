import dataclasses
from datetime import datetime
from random import randint

from backend.data.models.user import User
from backend.data.models.enroll import Enrollment


def generate_student_id():
    timestamp = int(datetime.now().timestamp() * 10)
    return f"STUD_{timestamp}{randint(100, 999)}"

@dataclasses
class Student(User):
    id:str = dataclasses.field(default_factory=generate_student_id)
    enrolled_course: Enrollment = dataclasses.field(init=False)