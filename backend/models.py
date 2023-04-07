from datetime import datetime

from sqlalchemy import Column, Boolean, String, DateTime, Integer, Text, ForeignKey

from core.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    is_active_subscription = Column(Boolean, default=True)

    def __repr__(self) -> str:
        return self.email


class Message(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.utcnow)
    PAO = Column(Boolean, default=True)
    DZO = Column(Boolean, default=True)
    subject = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    author = Column(Integer, ForeignKey(User.id))

    def __repr__(self) -> str:
        return self.subject
