
from typing import List

from model.db import db
from model.phase import Phase


class Schedule:
    def __init__(self, id_schedule: int, name: str):
        self.id_schedule: id_schedule
        self.name: name
        self.phases: List[Phase]


def save(schedules: List[Schedule]):
    for schedule in schedules:
        db.test_schedule.insert_one(schedule.__dict__)


def find_all() -> List[Schedule]:
    cursor = db.test_schedule.find()
    schedules = []
    for schedule in cursor:
        new_schedule = Schedule(
            schedule['id_schedule'],
            schedule['name']
        )
        schedules.append(new_schedule)
    return schedules

