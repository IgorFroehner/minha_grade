
from typing import List
from model.subject_dao import Subject

from app import db


class Phase(db.EmbeddedDocument):
    phase_number = db.IntField()
    subjects = db.ListField(db.EmbeddedDocumentField('Subject'))

    # def __init__(self, phase_number: int, *args, **values):
    #     super().__init__(*args, **values)
    #     self.phase_number: int = phase_number
    #     self.subjects: List[Subject] = []

    def set_subjects(self, subjects: List[Subject]):
        self.subjects = subjects

    def add_subject(self, subject: Subject):
        self.subjects.append(subject)

    def add_subjects(self, subjects: List[Subject]):
        self.subjects += subjects
