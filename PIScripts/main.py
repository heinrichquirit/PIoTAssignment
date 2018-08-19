import sys
import sqlite3 as lite
from crontab import CronTab
from sense_hat import SenseHat
from datetime import datetime
from insert_data import *

sense = SenseHat()

#connect to database
con = lite.connect('sensehat.db')

#table structure
# daterecorded  humidity  temperature
with con: 
    cur = con.cursor() 
    cur.execute("CREATE TABLE IF NOT EXISTS SENSEHAT_data(daterecorded DATETIME, temperature NUMERIC, humidity NUMERIC)")

#insert data
main()

#log data in a scheduler
    #insert into database

# Run scheduled repeating task

#setup cron job to pull data from sense hat at a specific time interval

#display data over a period using web interface


