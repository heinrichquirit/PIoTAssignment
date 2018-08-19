import bluetooth
import os
from sense_hat import SenseHat

#find the string "Pi" in device
def raspberryDevices(pi):
  if ("MARTIN") or ("Martin") in pi:
    print(pi)
  else:
    print("No devices named pi")

#search for nearby bluetooth devices
def search():
  nearby_devices = bluetooth.discover_devices()
  print("Here are all the nearby devices")
  for x in nearby_devices:
    devices = str(bluetooth.lookup_name(x)) + " [" + str(x) + "]"
    device_name = (bluetooth.lookup_name(x))
    print(devices)

  if ("MARTIN")  or  ("Martin") in device_name:
    print ("")
    sense = SenseHat()
    temp = round(sense.get_temperature(), 1)
    sense.show_message("Hello {}! The Temperature is {}".format(device_name, temp), scroll_speed=0.05, text_colour=(0, 0, 255))

  print("Here are all the Raspberry Pi Devices")
  print(raspberryDevices(devices))

#main function
def main():
  search()

#execute program
main()
