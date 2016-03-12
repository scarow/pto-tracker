from app.models import Base
from sqlalchemy import Column, Integer, String, Boolean, Date


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40))
    email = Column(String(40))
    passwd = Column(String(40))
    role = Column(String(40))
    start_date = Column(Date)
    end_date = Column(Date)
    pto_hours = Column(Integer)
    per_year = Column(Integer)
    active = Column(Boolean)

    def __init__(self, name, email):
        self.name = name
        self.email = email
