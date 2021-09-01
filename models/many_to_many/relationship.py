from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

from models.base import Base


AssociationTable = Table("association", Base.metadata,
                         Column("parent_id", ForeignKey('parentmtm.id'), primary_key=True),
                         Column("child_id", ForeignKey('childmtm.id'), primary_key=True)
                         )


class ParentMTM(Base):
    id = Column(Integer, primary_key=True)
    children = relationship("ChildMTM",
                            secondary=AssociationTable)


class ChildMTM(Base):
    id = Column(Integer, primary_key=True)
