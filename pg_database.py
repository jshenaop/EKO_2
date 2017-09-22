# coding=utf-8

### Database connector for Eko project ###
from datetime import datetime

import sqlalchemy
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, Integer, Numeric, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('postgresql://gestion:c0m1s10nCRC*@localhost/gestion', pool_recycle=1800)


Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Prediction(Base):
    """A base model to store Predictions """

    __tablename__ = 'predictions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(500))
    prediction_topic = Column(String(500))
    prediction_subtopic = Column(String(500))
    prediction_sub_subtopic = Column(String(500))
    gender = Column(String(500), default='')
    age = Column(String(500), default='')
    sentiment = Column(String(500), default='')
    datetime = Column(DateTime(), default=datetime.now)

Base.metadata.create_all(engine)


""" App user functions """

def add_query(text, prediction_topic, prediction_subtopic, prediction_sub_subtopic, gender, age, sentiment):
    cc_query = Prediction(text=text, prediction_topic=prediction_topic,
                                 prediction_subtopic=prediction_subtopic,
                                 prediction_sub_subtopic=prediction_sub_subtopic,
                                 gender=gender, age=age, sentiment=sentiment)
    session.add(cc_query)
    session.commit()

if __name__ == '__main__':
    add_query(text='Text', prediction_topic='Prediction', prediction_subtopic='Subtopic',
              prediction_sub_subtopic='subsubtopic', gender='gender', age='age', sentiment='sentiment')
