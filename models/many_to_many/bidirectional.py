from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

from models.base import Base


BidirectionalAssociationTable = Table("bidirectionalassociation", Base.metadata,
                                      Column("parent_id", ForeignKey('bidirectionalparentmtm.id'), primary_key=True),
                                      Column("child_id", ForeignKey('bidirectionalchildmtm.id'), primary_key=True)
                                      )


class BidirectionalParentMTM(Base):
    id = Column(Integer, primary_key=True)
    children = relationship("BidirectionalChildMTM",
                            secondary=BidirectionalAssociationTable,
                            back_populates="parents")


class BidirectionalChildMTM(Base):
    id = Column(Integer, primary_key=True)
    parents = relationship("BidirectionalParentMTM",
                           secondary=BidirectionalAssociationTable,
                           back_populates="children")
