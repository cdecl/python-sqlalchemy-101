from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta
import os

engine = create_engine('mysql+pymysql://dev:{}@localhost:3380/glass'.format(os.getenv("DB_PASSWD")))
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

engine_to = create_engine('mysql+pymysql://dev:{}@localhost:3380/glass'.format(os.getenv("DB_PASSWD")))
session_to = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine_to))

row2dict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}