# python-sqlalchemy-101

```sh
$ sqlacodegen mysql+pymysql://dev:$DB_PASSWD@localhost:3380/glass
# coding: utf-8
from sqlalchemy import Column, String, Table, Text
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class TblCode(Base):
    __tablename__ = 'tblCode'

    code = Column(String(128), primary_key=True)
    codename = Column(String(128))
    etc = Column(String(128))


class TblCodeTo(Base):
    __tablename__ = 'tblCode_to'

    code = Column(VARCHAR(128), primary_key=True)
    codename = Column(VARCHAR(128))
    etc = Column(VARCHAR(128))
```