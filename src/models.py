from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Speaker(Base):
    __tablename__ = "speakers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    bio = Column(String)
    company = Column(String)

    talks = relationship("Talk", back_populates="speaker")

class Talk(Base):
    __tablename__ = "talks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    speaker_id = Column(Integer, ForeignKey("speakers.id"))
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    speaker = relationship("Speaker", back_populates="talks")