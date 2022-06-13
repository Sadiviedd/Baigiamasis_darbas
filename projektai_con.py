from projektai import Projektai
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///projektai.db')
Session = sessionmaker(bind=engine)
session = Session()


def add_record(project, issue, worker, start_date, time_worked, end_date):
    record = Projektai(project, issue, worker, start_date, time_worked, end_date)
    session.add(record)
    session.commit()


def delete_record(record_id):
    record = session.query(Projektai).get(record_id)
    session.delete(record)
    session.commit()


def all_records():
    records = session.query(Projektai).all()
    return records