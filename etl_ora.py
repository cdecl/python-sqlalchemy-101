
from session_ora import SelectOp, EtlOp
from model.ora_member import Customer, CustomerTo


def main():
    rs = SelectOp(Customer, """
        SELECT * FROM Customer
    """)

    EtlOp(rs, None, CustomerTo)
    
if __name__ == "__main__":
    main()
    