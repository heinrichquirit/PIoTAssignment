import bluetooth

def raspberryDevices(device):
  if "MacBook" in device:
    return device

def search():
  nearby_devices = bluetooth.discover_devices()
  for bdaddr in nearby_devices[0:5]:
    print (str(bluetooth.lookup_name( bdaddr )) + " [" + str(bdaddr) + "]")
    print(raspberryDevices(bdaddr))

search()
