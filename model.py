
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Code(Base):
    __tablename__ = 'tblCode'
    code = Column(String, primary_key=True)
    codename = Column(String)

    def __init__(self, code, codename):
        self.code = code
        self.codename = codename 

