from .base import Base

# =================================================================
# One-to-many
from models.one_to_many.relationship import ParentOTM, ChildOTM

# Bidirectional behavior
from models.one_to_many.bidirectional import BidirectionalParentOTM, BidirectionalChildOTM
# =================================================================


# =================================================================
# Many-to-one
from models.many_to_one.relationship import ParentMTO, ChildMTO
# Bidirectional behaviour
from models.many_to_one.bidirectional import BidirectionalParentMTO, BidirectionalChildMTO
# =================================================================


# =================================================================
# One-to-one
from models.one_to_one.relationship import ParentOTO, ChildOTO
# =================================================================


# =================================================================
# Many-to-many
from models.many_to_many.relationship import AssociationTable, ParentMTM, ChildMTM
# Bidirectional behaviour
from models.many_to_many.bidirectional import BidirectionalAssociationTable, BidirectionalParentMTM, BidirectionalChildMTM
# =================================================================
