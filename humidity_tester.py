import sys
from sense_hat import SenseHat
import sqlite3 as lite

sense = SenseHat()

#record temperature every hour
humidity = sense.get_humidity()
temperature = sense.get_temperature()

#connect to database
con = lite.connect('sensehat.db')

#table structure
# daterecorded  humidity  temperature
with con: 
    cur = con.cursor() 
    cur.execute("CREATE TABLE IF NOT EXISTS SENSEHAT_data(daterecorded DATETIME, temperature NUMERIC, humidity NUMERIC)")

#log data in a scheduler
    #insert into database

#setup cron job to pull data from sense hat at a specific time interval

#display data over a period using web interface


