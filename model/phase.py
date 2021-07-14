
from typing import List
from model.subject import Subject


class Phase:
    def __init__(self, phase_number: int):
        self.phase_number: int = phase_number
        self.subjects: List[Subject] = []

    def set_subjects(self, subjects: List[Subject]):
        self.subjects = subjects

    def add_subject(self, subject: Subject):
        self.subjects.append(subject)

    def add_subjects(self, subjects: List[Subject]):
        self.subjects += subjects
