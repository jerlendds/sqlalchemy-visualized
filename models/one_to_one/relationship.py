from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base


class ParentOTO(Base):
    id = Column(Integer, primary_key=True)
    child = relationship("ChildOTO", back_populates="parent", uselist=False)


class ChildOTO(Base):
    id = Column(Integer, primary_key=True)
    # notice unique constraint, only one child may refer to a parent at a time
    parent_id = Column(Integer, ForeignKey('parentoto.id'), unique=True)
    parent = relationship("ParentOTO", back_populates="child")

