
from typing import List, Optional

from model import db
from model.phase import Phase


class Schedule:
    def __init__(self, id_schedule: int, name: str):
        self.id_schedule: int = id_schedule
        self.name: str = name
        self.phases: List[Phase] = []

    def set_phases(self, phases: List[Phase]):
        self.phases = phases

    def add_phase(self, phase: Phase):
        self.phases.append(phase)


def save(schedules: List[Schedule]):
    for schedule in schedules:
        save_one(schedule)


def save_one(schedule: Schedule):
    schedule_dict = schedule.__dict__
    print(schedule_dict)
    db.schedule.insert_one(schedule_dict)


def find_all(filter_schedule: dict = None) -> List[Schedule]:
    if filter_schedule is None:
        filter_schedule = {}
    cursor = db.schedule.find(filter_schedule)
    schedules = []
    for schedule in cursor:
        new_schedule = Schedule(
            schedule['id_schedule'],
            schedule['name']
        )
        schedules.append(new_schedule)
    return schedules


def find_one(filter_schedule: dict = None) -> Optional[Schedule]:
    if filter_schedule is None:
        filter_schedule = {}
    print(filter_schedule)
    returned_schedule = db.schedule.find_one(filter_schedule)
    print(returned_schedule)
    if returned_schedule is None:
        return None
    new_schedule = Schedule(
        returned_schedule['id_schedule'],
        returned_schedule['name']
    )
    return new_schedule
