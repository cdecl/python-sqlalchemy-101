
from session_ora import SelectOp, EtlOp
from model.ora_member import *

def main():
    rs = SelectOp(TestNull, """
        SELECT * FROM test_null
    """)

    EtlOp(rs, None, TestNullTo)
    
if __name__ == "__main__":
    main()
    