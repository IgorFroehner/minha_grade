
from typing import List
from model.subject import Subject

from mongoengine import Document, IntField, ListField, ReferenceField


class Phase(Document):
    phase_number = IntField()
    subjects = ListField(ReferenceField(Subject))

    def __init__(self, phase_number: int, *args, **values):
        super().__init__(*args, **values)
        self.phase_number: int = phase_number
        self.subjects: List[Subject] = []

    def set_subjects(self, subjects: List[Subject]):
        self.subjects = subjects

    def add_subject(self, subject: Subject):
        self.subjects.append(subject)

    def add_subjects(self, subjects: List[Subject]):
        self.subjects += subjects
