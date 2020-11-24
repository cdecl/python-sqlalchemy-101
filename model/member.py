
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Customer(Base):
    __tablename__ = 'Customer'

    ID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Address = Column(String(255))
    MobileNo = Column(String(100))
    Email = Column(String(255))
    BOD = Column(String(255))


class CustomerTo(Base):
    __tablename__ = 'CustomerTo'

    ID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Address = Column(String(255))
    MobileNo = Column(String(100))
    Email = Column(String(255))
    BOD = Column(String(255))