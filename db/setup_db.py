import pymysql
import csv


# setup connection and database
host = "wetttdb.cy4gcd1aoagq.us-east-1.rds.amazonaws.com"
port = 3306
user = "admin"
password = "cs5224cloudcomputing"
dbname = "wettt"

conn = pymysql.connect(host, user=user, port=port, passwd=password, cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

print("dropping existing database")
cur.execute('drop database wettt')

print("creating database: wettt")
cur.execute('create database wettt')
cur.execute("use wettt")

# malls table
print("creating table: malls")
cur.execute(
"""
create table malls(
mid int primary key,
name text,
district text,
address text,
description text)
"""
)

print("loading data into malls")
with open("malls.tsv", 'r') as f:
    data = csv.reader(f, delimiter="\t", quotechar='"')
    for row in list(data)[1:]:
        insert_query = """insert into malls (mid, name, district, address, description) 
                          VALUES ({}, "{}", "{}", "{}", "{}")""".format(int(row[0]), row[1], row[2], row[3], row[4])         
        cur.execute(insert_query)

print("select * from malls limit 1:")
cur.execute("""select * from malls limit 1""")
result = cur.fetchall()
for i in result:
    print(i)

# restaurants table
print("creating table: restaurants")
cur.execute(
"""
create table restaurants(
rid int primary key,
mid int,
name text,
cuisine text,
is_halal text,
is_veg text,
unit text,
phone text,
hours text,
description text,
website text,
pic_url text,
ad text
)
"""
)

print("loading data into restaurants")
with open("restaurants.tsv", 'r') as f:
    data = csv.reader(f, delimiter="\t", quotechar='"')
    for row in list(data)[1:]:
        insert_query = """insert into restaurants (rid, mid, name, cuisine, is_halal, is_veg, unit, phone, hours, description, website, pic_url, ad) 
                          VALUES ({}, {}, "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")""".format(
                          int(row[0]), int(row[1]), row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])         
        cur.execute(insert_query)

print("select * from restaurants limit 1:")
cur.execute("""select * from restaurants limit 1""")
result = cur.fetchall()
for i in result:
    print(i)

# promotions table
print("creating table: promotions")
cur.execute(
"""
create table promotions(
pid int primary key,
rid int,
bank text,
card text,
promo text)
"""
)

print("loading data into promotions")
with open("promotions.tsv", 'r') as f:
    data = csv.reader(f, delimiter="\t", quotechar='"')
    for row in list(data)[1:]:
        insert_query = """insert into promotions (pid, rid, bank, card, promo) 
                          VALUES ({}, {}, "{}", "{}", "{}")""".format(int(row[0]), int(row[1]), row[2], row[3], row[4])         
        cur.execute(insert_query)

print("select * from promotions limit 1:")
cur.execute("""select * from promotions limit 1""")
result = cur.fetchall()
for i in result:
    print(i)

# cuisine_types table
print("creating table: cuisine_types")
cur.execute(
"""
create table cuisine_types(
cid int primary key,
cuisine_type text)
"""
)

print("loading data into cuisine_types")
with open("cuisine_types.tsv", 'r') as f:
    data = csv.reader(f, delimiter="\t", quotechar='"')
    for row in list(data)[1:]:
        insert_query = """insert into cuisine_types (cid, cuisine_type) 
                          VALUES ({}, "{}")""".format(int(row[0]), row[1])         
        cur.execute(insert_query)

print("select * from cuisine_types limit 1:")
cur.execute("""select * from cuisine_types limit 1""")
result = cur.fetchall()
for i in result:
    print(i)

