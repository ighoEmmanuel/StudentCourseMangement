import dataclasses
from dataclasses import dataclass, field
from datetime import datetime
from random import randint

from backend.data.models.user import User
from backend.data.models.course import Course

def generate_prof_id():
    timestamp = int(datetime.now().timestamp() * 10)
    return f"PROF_{timestamp}{randint(100, 999)}"

@dataclass
class Professor(User):
    course: Course = dataclasses.field(init=False)
    id:str = field(default_factory=generate_prof_id)

