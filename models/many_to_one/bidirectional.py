from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models import Base


class BidirectionalParentMTO(Base):
    id = Column(Integer, primary_key=True)
    children = relationship("BidirectionalChildMTO", back_populates="parent")


class BidirectionalChildMTO(Base):
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('bidirectionalparentmto.id'))
    parent = relationship("BidirectionalParentMTO", back_populates="children")
