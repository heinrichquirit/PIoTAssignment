import bluetooth
import os
from sense_hat import SenseHat

#find the string "Raspberry" in device
def raspberryDevices(pi):
  if "Raspberry Pi" in pi:
    print(pi)
  else:
    print("No Raspberry Pi devices nearby")

#search for nearby bluetooth devices. Print them out and greet all raspberry pi devices on the Sense Hat
def search():
  nearby_devices = bluetooth.discover_devices()
  print("Here are all the nearby devices")
  for x in nearby_devices:
    devices = str(bluetooth.lookup_name(x)) + " [" + str(x) + "]"
    device_name = (bluetooth.lookup_name(x))
    print(devices)
  
    print ("")  
    print("Here are all the Raspberry Pi Devices")
    print(raspberryDevices(devices))

  if "Raspberry Pi" in device_name:
    sense = SenseHat()
    temp = float(sense.get_temperature())
    cpu_temp = float(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3
    calibrated_temp = round(cpu_temp - temp, 2)
    sense.show_message("Hello {}! The Temperature is {}".format(device_name, calibrated_temp), scroll_speed=0.05, text_colour=(0, 0, 255))

#main function
def bt_main():
  search()

#execute program
bt_main()
