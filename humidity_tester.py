import sense_hat from SenseHat
sense = SenseHat()

#record temperature every hour
float humidity = sense.get_humidity()
float temperature = sense.get_temperature()

#table structure
#             humidity  temperature
# timestamp

#connect to database
#martin test commit

#log data in a scheduler
    #insert into database

#setup cron job to pull data from sense hat at a specific time interval

#display data over a period using web interface


