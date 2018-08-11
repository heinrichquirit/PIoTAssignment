from sense_hat import SenseHat
import requests
import json
import os

sense = SenseHat()
sense.clear()

temp = sense.get_temperature()
sense.clear()

ACCESS_TOKEN="o.OWFLOnAYou7KFqhOrdXmW3MQQenSVBqN"

def send_notification_via_pushbullet(title, body):
    """ Sending notification via pushbullet.
        Args:
            title (str) : title of text.
            body (str) : Body of text.
    """
    data_send = {"type": "note", "title": title, "body": body}
 
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + ACCESS_TOKEN, 
                         'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('complete sending')

#main function
def main():
    send_notification_via_pushbullet(str(temp), "Bring a Sweater")

def main2():
    send_notification_via_pushbullet(str(temp), "Leave that sweater at home")


if temp < 20:
    print("Temp is: " + str(temp) + "bring a sweater")
    main()
else:
    print("leave that sweater at home")
    main2()
