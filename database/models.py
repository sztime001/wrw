from sqlalchemy import Column, Integer, String
from .dbconfig import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=False, nullable=False)
    email = Column(String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username