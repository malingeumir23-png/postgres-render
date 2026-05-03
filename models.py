from sqlalchemy import Column, Integer, String
from database import Base

class Character(Base):
    __tablename__ = "character"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    actor = Column(String, index=True)
