# coding: utf-8
from sqlalchemy import Column, Integer, VARCHAR, text
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

