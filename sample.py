from sqlalchemy.sql import text
from session import session, session_to, row2dict
from model.member import Customer, CustomerTo

def InsertOp():
    cust = Customer()
    cust.ID = 1000
    session.add(cust)
    session.commit()
    SelectOp()

def UpdateOp():
    cust = session.query(Customer).filter(Customer.ID=='1000').first()
    cust.Name = "BK KIM"
    session.commit() 
    SelectOp()   

def MergeOp():
    cust = Customer()
    cust.ID = 1000
    cust.Name = "Byung Kyu"
    session.merge(cust)
    session.commit()   
    SelectOp()   

def DeleteOp():
    session.query(Customer).filter(Customer.ID == 1000).delete()
    session.commit()

def SelectOp():
    rs = session.query(Customer)
    # rs = session.query(Customer).filter(Customer.Name.op('regexp')('Jason.*'))
    # rs = session.query(Customer).filter(Customer.ID < 10)
    # rs = session.query(Customer).from_statement(text("""
    #     SELECT  * FROM Customer WHERE ID < 10 
    # """))

    for r in rs:
        d = row2dict(r)
        print(d)

def main():
    # InsertOp()
    # UpdateOp()
    # MergeOp()
    # DeleteOp()
    SelectOp()

    
if __name__ == "__main__":
    main()
    