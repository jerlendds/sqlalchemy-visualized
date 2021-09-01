from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base


class ParentOTM(Base):
    id = Column(Integer, primary_key=True)
    children = relationship("ChildOTM")


class ChildOTM(Base):
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parentotm.id'))

