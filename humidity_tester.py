import sys
import sqlite3 as lite
from crontab import CronTab
from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()

#init cron
cron = CronTab(user='pi')
cron.remove_all()

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
time = datetime.now().strftime("%H:%M")

#add new cron job
job = cron.new(command='record_data.py')

#job settings
job.minute.every(1)
cron.write()

#setup cron job to pull data from sense hat at a specific time interval

#display data over a period using web interface


