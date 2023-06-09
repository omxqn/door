import evdev

# Set the name of the RFID reader
rfid_device_name = 'MyRFIDReader'

# Find the input device with the given name
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
rfid_device = None
for device in devices:
    if device.name == rfid_device_name:
        rfid_device = device
        break

# If the RFID reader was found, read from it
if rfid_device is not None:
    print('Found RFID reader:', rfid_device.name)
    for event in rfid_device.read_loop():
        if event.type == evdev.ecodes.EV_KEY and event.value == 1:
            print('RFID tag scanned:', evdev.categorize(event).keycode)
else:
    print('RFID reader not found.')
