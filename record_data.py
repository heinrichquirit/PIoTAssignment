from humidity_tester import *

sql2 = "insert into SENSEHAT_data(NULL, 11.1, 22.2)"
sql = "insert into SENSEHAT_data ({}, {}, {})".format(time, temperature, humidity)

print("test")
cur = con.cursor()
cur.execute(sql2)
print("Writing data...")