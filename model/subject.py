
from typing import List


class Subject:
    def __init__(self):
        self.id_subject: str
        self.workload: int
        self.optional: bool
        self.requirements: List[Subject]
