# python-sqlalchemy-101

## MySQL

### sqlacodegen

```sh
$ sqlacodegen mysql+pymysql://dev:$DB_PASSWD@localhost:3380/glass
# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Customer(Base):
    __tablename__ = 'Customer'

    ID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Address = Column(String(255))
    MobileNo = Column(String(100))
    Email = Column(String(255))
    BOD = Column(String(255))


class CustomerTo(Base):
    __tablename__ = 'CustomerTo'

    ID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Address = Column(String(255))
    MobileNo = Column(String(100))
    Email = Column(String(255))
    BOD = Column(String(255))
```

## Oracle

### cx_Oracle 패키지 설치

```sh
$ pip install cx_oracle
```

### Oracle Client 설치 
- https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html

```sh
$ curl -O https://download.oracle.com/otn_software/linux/instantclient/199000/instantclient-basic-linux.x64-19.9.0.0.0dbru.zip
$ unzip instantclient-basic-linux.x64-19.9.0.0.0dbru.zip
$ sudo mv instantclient_19_9 /usr/lib/

$ cat <<EOF > /etc/ld.so.conf.d/oracle_client.conf
> /usr/lib/instantclient_19_9:
> EOF 

$ sudo ldconfig -v
```
### libaio 설치
```sh
$ sudo apt-get install libaio1
```

### sqlacodegen

```sh
$ sqlacodegen "oracle+cx_oracle://system:oracle@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SID=xe)))" --tables customer
# coding: utf-8
from sqlalchemy import Column, Integer, VARCHAR, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), server_default=text("NULL"))
    address = Column(VARCHAR(255), server_default=text("NULL"))
    mobileno = Column(VARCHAR(100), server_default=text("NULL"))
    email = Column(VARCHAR(255), server_default=text("NULL"))
    bod = Column(VARCHAR(255), server_default=text("NULL"))
```
---

### Oracle Docker 

```sh
$ docker run -d -p 8080:8080 -p 1521:1521 --name=oracle truevoly/oracle-12c
```