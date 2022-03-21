# İBB Ulaşım Verilerinin İncelenmesi

Proje içinde:
- CKAN API
- PostgreSQL
- psql, DBbeaver
- Apache Superset
- CSV
- Pandas, psycopg2

kullanılacaktır. Bu projede amacım bu zamana kadar kendimi geliştirdiğim bazı konularda uygulama yapmaktır. Proje içeriği zamanla güncellenecektir.

[![CKAN](https://i.ibb.co/L9vmRZ9/f0a9090f9c0f3135354ceca1e202e945.png "CKAN")](https://i.ibb.co/L9vmRZ9/f0a9090f9c0f3135354ceca1e202e945.png "CKAN") [![PostgreSQL](https://cdn.iconscout.com/icon/free/png-256/postgresql-11-1175122.png "PostgreSQL")](https://cdn.iconscout.com/icon/free/png-256/postgresql-11-1175122.png "PostgreSQL") [![Superset](https://i.ibb.co/QHzRP7Q/superset-icon-e1612039883795-25.png "Superset")](https://i.ibb.co/QHzRP7Q/superset-icon-e1612039883795-25.png "Superset") [![dbeaver](https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco,dpr_1/ssrytpiyexobjhlo77ew "dbeaver")](https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco,dpr_1/ssrytpiyexobjhlo77ew "dbeaver")

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
Çektiğimiz verileri bir veritabanına yazıp daha sonra Apache Superset ile inceleyeceğiz.

Veritabanı oluşturma işlemi psycopg2 yerine psql, pgAdmin, DBeaver araçları ile de yapılabilir.

Connection işlemini veritabanını oluşturduktan sonra ibb_ulasim'a bağlanacak şekilde güncelliyoruz.

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
    "NUMBER_OF_PASSENGER" INTEGER,
    "NUMBER_OF_PASSAGE" INTEGER)
    """

cursor.execute(table_create)
```

```python
cursor.execute("Select * FROM ulasim LIMIT 0")
# Checking the column names
colnames = [desc[0] for desc in cursor.description]
print(colnames)
```
```python
['id', 'DATE_TIME', 'TIME', 'TRANSPORT_TYPE_ID', 'TRANSPORT_TYPE_DESC', 'LINE', 'TRANSFER_TYPE_ID', 'TRANSFER_TYPE', 'NUMBER_OF_PASSENGER', 'NUMBER_OF_PASSAGE']
```
##### Çektiğimiz verilerde ID sütunu kullanılmayacaktır, ID'yı SERIAL olarak Postgre kendisi atayacaktır. 
--------------------------------------
## CKAN, CKAN API
CKAN Open Knowledge Foundation tarafından geliştirilen verilerin paylaşımını, kullanımını ve bulunmasını kolaylaştıran open source veri yönetim sistemidir. Çeşitli hükümetler ve şirketlere ait 15 milyondan fazla veri seti bulundurmaktadır. CKAN alt yapısı ile birlikte, verileri pek çok formatta paylaşıp aynı zamanda web sitesi üzerinden recline_graph_view, recline_map_view gibi eklentiler ile verilerin interaktif görselleştirmesini yapabiliriz.

CKAN API ile verileri JSON, XML, CSV, TSV formatında çekebiliriz. Ayrıca 'datastore_search_sql' ile SQL sorgularını kullanarak veri talebi yapmamıza olanak vermektedir.

Projede DataStore eklentisini kullanarak çeşitli veri setleri çekilecektir. CSV dosyaları için `?bom=true` , JSON için `?format=json` parametreleri kullanılabilir.

```python
import pandas as pd
dump_links = ["https://data.ibb.gov.tr/datastore/dump/511c5034-0a1c-4c77-9831-157f30e62aee?bom=True",
              "https://data.ibb.gov.tr/datastore/dump/de831d1d-85a3-478e-8167-72223ee7ffaa?bom=True",
              "https://data.ibb.gov.tr/datastore/dump/fb49c73d-f0f5-439c-ad7b-64f3494a2d9f?bom=True",
              "https://data.ibb.gov.tr/datastore/dump/75e25417-36df-4822-8a18-578f0f7a584a?bom=True",
              "https://data.ibb.gov.tr/datastore/dump/3497a04f-5b78-44f3-8bdc-8c30ab19af88?bom=True",
              "https://data.ibb.gov.tr/datastore/dump/4f1c434d-bd1f-4937-b88f-6e2df1a85dc5?bom=True",
              "https://data.ibb.gov.tr/datastore/dump/0fdf0efb-2ae3-4ff5-a106-0c6c7392f6d4?bom=True",
              "https://data.ibb.gov.tr/datastore/dump/a195a42f-727a-4f1e-ad55-471306788c99?bom=True",
              "https://data.ibb.gov.tr/datastore/dump/5b3b12b7-575d-4b55-b497-62e3b544edb0?bom=True",
              "https://data.ibb.gov.tr/datastore/dump/d5b65aa8-8cf0-4034-a827-17e170894b38?bom=True",
              "https://data.ibb.gov.tr/datastore/dump/4691d5de-689e-4b0a-b5e7-5e54f893edfc?bom=True",
              "https://data.ibb.gov.tr/datastore/dump/0d822ea9-bd44-4f09-a2aa-27f1b37e4538?bom=True"]

# Storing all dataframes
dfs = [pd.read_csv(url) for url in dump_links]
# Merging dataframes in dfs
df = pd.concat(dfs, ignore_index=True)
df_drop_id = df.drop(["_id"], axis=1)
df_drop_id.to_csv("test.csv",index=False)
```
Tek bir dosyada birleştirdiğimiz verilerimizi, veritabanına kaydedeceğiz. İlk aşamada psycopg2 ile PostgreSQL'deki "COPY" işlevini kullanmaya çalıştım ancak bu çeşitli yetki hataları ile sonuçlanmakta, işlemi yapan kullanıcı Super User yetkisine de sahip olsa ve/veya veri Temp klasörü gibi bir yerden de çekilse yetki hataları devam etmekte. Bu sorun psql ile giderilebilir:
## psql Aracılığı İle CSV Dosyasındanki Verileri Veritabanına Taşımak
`psql -U <kullanıcı adı>` komutu ile ilgili kullanıcı ile psql üzerinden işlemlerimizi gerçekleştirebiliriz. `\l` ile veritabanlarının listesini erişip `\c <veritabanı adı>` ile ilgili veritabanına bağlanabiliriz.

CSV dosyasını veritabanına aktarırken dikkat etmemiz gereken bazı hususlar mevcut, ilgili komutu paylaştıktan sonra bunları açıklayacağım:

`\copy ulasim("DATE_TIME","TRANSPORT_TYPE_ID","TRANSPORT_TYPE_DESC","LINE","TRANSFER_TYPE_ID","TRANSFER_TYPE", "NUMBER_OF_PASSENGER","NUMBER_OF_PASSAGE") FROM 'C:\\Users\\acs\\Desktop\\ibb\\test.csv' DELIMITER ',' CSV ENCODING 'UTF8' HEADER;`

COPY işlevini kullanırken eğer mevcut verilerimiz ASCII formatına uygun olmayan karakterler barındırıyorsa ENCODING parametresi ile uygun encoding türünü belirleyebiliriz. Bizim veri setimizde böyle bir durum mevcuttu:

[![csv](https://i.ibb.co/DVZXgpg/csv.png "csv")](https://i.ibb.co/DVZXgpg/csv.png "csv")

Hangi sütunlardaki verilerin veritabanına geçeceğine tablo ismi("SütunAdı") şeklinde karar verebiliriz. Eğer büyük harfle veya boşluğa sahip sütun isimlerine sahipsek çift tırnak kullanımı olmadan yazmak sorunlar çıkarabilir. Bunun dışında CSV dosyasının yolu belirtilirken sağa yatık slash veya sola yatık çift slash kullanılmadığında hata dönebilmekte. 

