import sqlite3
conn = sqlite3.connect('test.db')
print("Connection /l ",conn)
# query1= """CREATE TABLE TEST1
# (ID INT,
# NAME VARCHAR)"""
# print(query1)
# conn.execute(query1)

# query2="""INSERT INTO TEST1
# (ID, NAME) VALUES (1,'ABC')"""
# conn.execute(query2)
# conn.commit()

query3="SELECT * FROM TEST1"
cur=conn.cursor()
cur.execute(query3)
row = cur.fetchall()
print(row)
for rows in row:
    print(rows)
conn.close()
