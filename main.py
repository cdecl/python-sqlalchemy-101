from sqlalchemy.sql import text
from session import session, session_to, row2dict
from model import TblCode, TblCodeTo

# def InsertOp():
#     code = TblCode('00006', 'Base code6')
#     session.add(code)
#     session.commit()
#     select()

# def UpdateOp():
#     code = session.query(TblCode).filter(TblCode.code=='00003').first()
#     code.codename = "3333"
#     session.commit()    

# def MergeOp():
#     code = TblCode('00005', 'code 545555')
#     session.merge(code)
#     session.commit()   

# def DeleteOp():
#     session.query(TblCode).filter(TblCode.code=='00001').delete()
#     session.commit()

def SelectOp():
    # rs = session.query(Code).filter(Code.code.op('regexp')('0000.*'))
    # rs = session.query(Code).filter(Code.code=='00005')
    rs = session.query(TblCode).from_statement(text("""
        select * from tblCode
    """))
    return rs

def Manip(data):
    # data['Etc'] = "pass-"
    pass

def EtlOp(SelectOp, Manip, TargetTable):
    rs = SelectOp()
    for r in rs:
        data = row2dict(r)
        Manip(data)
        newdata = TargetTable(**data)
        session_to.merge(newdata);
        print(data)
    session_to.commit()

def main():
    EtlOp(SelectOp, Manip, TblCodeTo)
    
if __name__ == "__main__":
    main()
    