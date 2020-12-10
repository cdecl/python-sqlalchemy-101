# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), server_default=text("NULL"))
    address = Column(VARCHAR(255), server_default=text("NULL"))
    mobileno = Column(VARCHAR(100), server_default=text("NULL"))
    email = Column(VARCHAR(255), server_default=text("NULL"))
    bod = Column(VARCHAR(255), server_default=text("NULL"))


class CustomerTo(Base):
    __tablename__ = 'customerto'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), server_default=text("NULL"))
    address = Column(VARCHAR(255), server_default=text("NULL"))
    mobileno = Column(VARCHAR(100), server_default=text("NULL"))
    email = Column(VARCHAR(255), server_default=text("NULL"))
    bod = Column(VARCHAR(255), server_default=text("NULL"))



class TestNull(Base):
    __tablename__ = 'test_null'

    id = Column(Integer, primary_key=True)
    etc = Column(VARCHAR(64))
    num = Column(NUMBER(asdecimal=False))
    dt = Column(DateTime)

class TestNullTo(Base):
    __tablename__ = 'test_null_to'

    id = Column(Integer, primary_key=True)
    etc = Column(VARCHAR(64))
    num = Column(NUMBER(asdecimal=False))
    dt = Column(DateTime)
