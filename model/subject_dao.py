from typing import List

from app import db


class Subject(db.EmbeddedDocument):
    id_subject = db.StringField()
    nome = db.StringField()
    workload = db.IntField()
    optional = db.BooleanField()
    ids_requirements = db.ListField(db.StringField())

    # def __init__(self, id_subject: str, nome: str, workload: int, optional: bool = False, ids_requirements=None, *args,
    #              **values):
    #     super().__init__(*args, **values)
    #     self.id_subject: str = id_subject
    #     self.nome: str = nome
    #     self.workload: int = workload
    #     self.optional: bool = optional
    #     if ids_requirements is None:
    #         ids_requirements = []
    #     self.ids_requirements: List[str] = ids_requirements

    def set_requirements(self, ids_requirements: List[str]):
        self.ids_requirements = ids_requirements

    def add_requirement(self, id_requirement: str):
        self.ids_requirements.append(id_requirement)
