from sense_hat import SenseHat
import requests
import json
import os

sense = SenseHat()
sense.clear()
temp = float(sense.get_temperature())
cpu_temp = float(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3
calibrated_temp = round(cpu_temp - temp, 2)

ACCESS_TOKEN="o.OWFLOnAYou7KFqhOrdXmW3MQQenSVBqN"

#sourced from canvas tutorial
#uses push bullet api to send notifcations to phone
def send_notification_via_pushbullet(title, body):
    data_send = {"type": "note", "title": title, "body": body}
 
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + ACCESS_TOKEN, 
                         'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('complete sending')

#main function
def push_main():
    if temp < 20:
        print("Temp={}'C Bring a Sweater!".format(calibrated_temp))
        send_notification_via_pushbullet(str(calibrated_temp), "Bring a Sweater!")
    else:
        print("Temp={}'C Leave that sweater at home!".format(calibrated_temp))
        send_notification_via_pushbullet(str(calibrated_temp), "Leave that sweater at home!")

#execute 
push_main()

