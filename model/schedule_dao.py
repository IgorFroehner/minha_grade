
from typing import List, Optional

from app import db
from model.phase_dao import Phase


class Schedule(db.Document):
    name = db.StringField()
    phases = db.ListField(db.EmbeddedDocumentField(Phase))

    # def __init__(self, name: str, *args, **values):
    #     super().__init__(*args, **values)
    #     self.name: str = name
    #     self.phases: List[Phase] = []

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
    return Schedule.objects(filter_schedule)


def find_one(filter_schedule: dict = None) -> Optional[Schedule]:
    if filter_schedule is None:
        filter_schedule = {}
    return Schedule.objects(__raw__=filter_schedule).first()


def find_by_id(id: str) -> Optional[Schedule]:
    try:
        return Schedule.objects.get(id=id)
    except Exception as e:
        return None
