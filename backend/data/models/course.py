from dataclasses import dataclass, field
from datetime import datetime
from random import randint

def generate_course_id():
    timestamp = int(datetime.now().timestamp() * 10)
    return f"CRS_{timestamp}{randint(100, 999)}"

@dataclass
class Course:
    course_name: str
    id: str = field(default_factory=generate_course_id)
