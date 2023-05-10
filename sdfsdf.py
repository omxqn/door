from evdev import InputDevice
from select import select

# Find the device path for the RFID reader (use "cat /proc/bus/input/devices" to get the device list)
rfid_device_path = '/dev/input/eventX'  # replace X with the appropriate device number

# Open the device for reading events
rfid_device = InputDevice(rfid_device_path)

# Read RFID tag events
while True:
    # Wait for an event to occur
    r, w, x = select([rfid_device], [], [])

    # Read the event
    for event in r:
        if event.type == 1 and event.value == 1:
            # RFID tag was detected
            tag_id = event.code
            print(f"RFID tag detected: {tag_id}")
