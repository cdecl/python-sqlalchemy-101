
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class TblCode(Base):
    __tablename__ = 'tblCode'

    code = Column(String(128), primary_key=True)
    codename = Column(String(128))
    Etc= Column(String(128))

    def __init__(self, code, codename):
        self.code = code
        self.codename = codename 

class TblCodeTo(Base):
    __tablename__ = 'tblCode_to'

    code = Column(String(128), primary_key=True)
    codename = Column(String(128))
    Etc= Column(String(128))