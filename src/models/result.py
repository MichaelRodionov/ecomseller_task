from sqlalchemy import Column, Integer, String

from src.core.db import Base


# ----------------------------------------------------------------
class ResultModel(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    item_id = Column(Integer, index=True, nullable=False)
    offer_id = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
