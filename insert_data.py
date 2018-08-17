# Sourced from canvas resources

import time
import sqlite3
from sense_hat import SenseHat
dbname='sensehat.db'
sampleFreq = 1 # time in seconds

# get data from SenseHat sensor
def getSenseHatData():	
    sense = SenseHat()
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
	
    if temp is not None and humidity is not None:
        temp = round(temp, 1)
        humidity = round(humidity, 1)
        logData (temp, humidity)

# log sensor data on database
def logData (temp, humidity):	
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    #need to change date time to UTC
    curs.execute("INSERT INTO SENSEHAT_data values(datetime('now'), (?), (?))", (temp, humidity))
    conn.commit()
    conn.close()

# display database data
def displayData():
    #display with column names
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    print ("\nEntire database contents:\n")
    print ("Time | Temperature (c) | Humidity\n")
    for row in curs.execute("SELECT * FROM SENSEHAT_data"):
        print (row)
    conn.close()

# main function
def main():
    for i in range (0,3):
        getSenseHatData()
        time.sleep(sampleFreq)
    displayData()

# Execute program 
main()
