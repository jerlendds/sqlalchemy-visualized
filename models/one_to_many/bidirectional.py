from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models import Base


class BidirectionalParentOTM(Base):
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey('bidirectionalchildotm.id'))
    child = relationship("BidirectionalChildOTM", back_populates='parents')


class BidirectionalChildOTM(Base):
    id = Column(Integer, primary_key=True)
    parents = relationship("BidirectionalParentOTM", back_populates='child')
