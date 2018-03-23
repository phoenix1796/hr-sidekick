import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    name = Column(
    String(80), nullable=False)
    password = Column(
        String(255), nullable=False)
    id = Column(
        Integer, primary_key = True
    )
class Result(Base):
    __tablename__ = 'result'
    inputs = Column(String(), nullable=False)
    id = Column(Integer, primary_key=True)
    result = Column(String())
    user_id = Column(
        Integer, ForeignKey('user.id')
    )
    user = relationship(User)
    @property
    def serialize(self):
        return {
            'inputs': self.inputs,
            'result':self.result,
            'id': self.id
        }

engine = create_engine(
    'sqlite:///hr_sidekick.db')
Base.metadata.create_all(engine)