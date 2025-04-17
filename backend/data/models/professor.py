import time
from dataclasses import dataclass
from random import random

from backend.data.models.user import User
from backend.data.models.course import Course


@dataclass
class Professor(User):
    __id = f"Pro_{int(time.time() * 1000)}{random.randint(1000,4000)}"
    __course: Course
