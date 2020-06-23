from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from model import Code

engine = create_engine('mysql+pymysql://glass:glasspasswd@infradb.inpark.kr:3380/glass')
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


def add():
    code = Code('00003', 'Base code4')
    session.add(code)
    session.commit()

def update():
    code = session.query(Code).filter(Code.code=='00003').first()
    code.codename = "3333"
    session.commit()    

def merge():
    code = Code('00005', 'code 545555')
    session.merge(code)
    session.commit()   

def delete():
    session.query(Code).filter(Code.code=='00001').delete()
    session.commit()

def select():
    # rs = session.query(Code).filter(Code.code.op('regexp')('0000.*'))
    # rs = session.query(Code).filter(Code.code=='00005')
    rs = session.query(Code).filter(Code.code.like('0000%'))
    for r in rs:
        print(r.code, r.codename)

def main():
    select()
    
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)


    