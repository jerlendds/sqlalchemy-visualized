from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base


class ParentMTO(Base):
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey('childmto.id'))
    child = relationship("ChildMTO")


class ChildMTO(Base):
    id = Column(Integer, primary_key=True)

