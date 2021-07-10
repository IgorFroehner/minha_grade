
from typing import List
from model.subject import Subject


class Phase:
    def __init__(self):
        self.phase_number: int
        self.subjects: List[Subject]
