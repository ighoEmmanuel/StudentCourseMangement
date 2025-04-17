import dataclasses
import time
from random import random

from backend.data.models.user import User
from backend.data.models.enroll import Enrollment


@dataclasses
class Student(User):
    id = f"Stu_{int(time.time() * 1000)}{random.randint(1000,4000)}"
    enrolled_course: Enrollment = dataclasses.field(init=False)