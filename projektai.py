from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///projektai.db')
Base = declarative_base()


class Projektai(Base):
    __tablename__ = 'Projektai'
    id = Column(Integer, primary_key=True)
    project_name = Column("Projektas", String)
    issue_id = Column("Uzduotis", String)
    worker_name = Column("Darbuotojas", String)
    start_date = Column("Darbo_pradzia", DateTime)
    time_worked = Column("Pradirbtas_laikas", String)
    end_date = Column("Darbo_pabaiga", DateTime)

    def __init__(self, project_name, issue_id, worker_name, start_date, time_worked, end_date):
        self.project_name = project_name
        self.issue_id = issue_id
        self.worker_name = worker_name
        self.start_date = start_date
        self.time_worked = time_worked
        self.end_date = end_date

    def __repr__(self):
        return f"{self.id}    " \
               f"{self.project_name}    " \
               f"{self.issue_id}    " \
               f"{self.worker_name}    " \
               f"{self.start_date}    " \
               f"{self.time_worked}    " \
               f"{self.end_date}"


Base.metadata.create_all(engine)