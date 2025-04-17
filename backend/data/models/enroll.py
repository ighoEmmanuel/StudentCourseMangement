from dataclasses import dataclass
from datetime import datetime

from backend.data.models.grade import Grade


@dataclass
class Enrollment:
    student_id: str
    course_id: str
    grade: Grade
    enrollment_date: datetime = datetime.now()

