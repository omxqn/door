import evdev

# Find the input device with the name "RFID reader"
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
rfid_device = None
for device in devices:
    print(device)
    if device.name == 'BARCODE SCANNER Keyboard Interface':
        rfid_device = device
        break
data = []

def read():
    # If the RFID reader was found, read from it
    if rfid_device is not None:
        if data == []:
            print('Found RFID reader:', rfid_device.name)
        global rfid_tag
        rfid_tag = ''
        for event in rfid_device.read_loop():
            if event.type == evdev.ecodes.EV_KEY and event.value == 1:
                digit = evdev.categorize(event).keycode
                if digit == "KEY_ENTER" :
                    if rfid_tag in data:
                        print(f"User with id: {rfid_tag} is in database and Enterd the gate")
                        break
                    else:
                        id = rfid_tag
                        rfid_tag = ""
                        print(f'RFID tag ({id}) has been added:')
                        data.append(id)

                        break
	    	
                else:

                   
                    if digit[-1].isdigit():
                        rfid_tag+= digit[-1]
    else:
        print('RFID reader not found.')

        
while True:
    read()
