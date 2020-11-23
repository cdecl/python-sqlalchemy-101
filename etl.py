
from session import SelectOp, EtlOp
from model.member import Customer, CustomerTo


def main():
    rs = SelectOp(Customer, """
        SELECT * FROM Customer
    """)

    EtlOp(rs, None, CustomerTo)
    
if __name__ == "__main__":
    main()
    