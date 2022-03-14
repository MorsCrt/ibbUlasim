# İBB Ulaşım Verilerinin İncelenmesi

Proje içinde:
- CKAN API
- PostgreSQL
- Apache Superset
-  JSON
- psycopg2, pprintpp
- Pandas, Numpy

kullanılacaktır. İçerik zamanla güncellenecektir.

[![CKAN](https://i.ibb.co/L9vmRZ9/f0a9090f9c0f3135354ceca1e202e945.png "CKAN")](https://i.ibb.co/L9vmRZ9/f0a9090f9c0f3135354ceca1e202e945.png "CKAN")

[![PostgreSQL](https://cdn.iconscout.com/icon/free/png-256/postgresql-11-1175122.png "PostgreSQL")](https://cdn.iconscout.com/icon/free/png-256/postgresql-11-1175122.png "PostgreSQL")

[![Superset](https://i.ibb.co/QHzRP7Q/superset-icon-e1612039883795-25.png "Superset")](https://i.ibb.co/QHzRP7Q/superset-icon-e1612039883795-25.png "Superset")

## Veritabanı Oluşturma:
```python
import psycopg2

#establishing the connection
try:
    conn = psycopg2.connect(
        database="postgres",
        user='postgres',
        password='44410',
        host='127.0.0.1',
        port='5432')
    conn.autocommit = True
except:
    print("Cannot connect to db")

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

cursor.execute('CREATE DATABASE ibb_ulasim')
```

Veritabanı oluşturma işlemi psycopg2 yerine psql, pgAdmin, DBeaver araçları ile de yapılabilir.

 ----------------------------------
## Tablo Oluşturma

```python
table_create = """
    CREATE TABLE ulasim(
    id SERIAL PRIMARY KEY,
    "DATE_TIME" DATE,
    "TIME" TIME,
    "TRANSPORT_TYPE_ID" SMALLINT,
    "TRANSPORT_TYPE_DESC" VARCHAR(8),
    "LINE" VARCHAR(50),
    "TRANSFER_TYPE_ID" SMALLINT,
    "TRANSFER_TYPE" VARCHAR(7),
    "NUMBER_OF_PASSENGER" SMALLINT,
    "NUMBER_OF_PASSAGE" SMALLINT)
    """

cursor.execute(table_create)
```
Tablo isimlerini kontrol edelim:
```python
cursor.execute("Select * FROM ulasim LIMIT 0")
colnames = [desc[0] for desc in cursor.description]
print(colnames)
```
```python
['id', 'DATE_TIME', 'TIME', 'TRANSPORT_TYPE_ID', 'TRANSPORT_TYPE_DESC', 'LINE', 'TRANSFER_TYPE_ID', 'TRANSFER_TYPE', 'NUMBER_OF_PASSENGER', 'NUMBER_OF_PASSAGE']


```
