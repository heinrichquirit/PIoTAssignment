import bluetooth
import os
from sense_hat import SenseHat

#find the string "Pi" in device
def raspberryDevices(pi):
  if ("Raspberry Pi") or ("Pi") in pi:
    print(pi)
  else:
    print("No Raspberry Pi devices nearby")

#search for nearby bluetooth devices
def search():
  nearby_devices = bluetooth.discover_devices()
  print("Here are all the nearby devices")
  for x in nearby_devices:
    devices = str(bluetooth.lookup_name(x)) + " [" + str(x) + "]"
    device_name = (bluetooth.lookup_name(x))
    print(devices)

  if ("Raspberry Pi") or ("Pi") in device_name:
    print ("")
    sense = SenseHat()
    temp = float(sense.get_temperature())
    cpu_temp = float(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3
    calibrated_temp = round(cpu_temp - temp, 2)
    sense.show_message("Hello {}! The Temperature is {}".format(device_name, calibrated_temp), scroll_speed=0.05, text_colour=(0, 0, 255))

  print("Here are all the Raspberry Pi Devices")
  print(raspberryDevices(devices))

#main function
def bt_main():
  search()

#execute program
bt_main()
