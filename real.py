from ipz_hid.linux.HID_linux_device import *
from ipz_hid.core.HID_usages import *

# Nový deskriptor ktorý zariadenie bude používať.
# Pozor: deskriptor nemení binárny formát reportu - zariadenie stále posiela rovnaké dáta,
# pomocou zmeneného deskriptoru je ale možné zmeniť ich význam.
new_descriptor: HIDDescriptor = HIDDescriptor([
# sem skopírujte upravený deskriptor s predošlej úlohy
])

def main():
    # nastavenia pre pripojenie k zariadeniu
    options = HIDLinuxDeviceOptions(
        attach_hidraw=True,
        make_virtual_device=True,
        grab_events=True,
    )
    # pripojenie k zariadeniu ktoré má v názve "Keyboard"
    device = HIDLinuxDevice.from_device_name("Keyboard", options)
    descriptor = device.get_descriptor()
    device.start()
    print("Attached to device. Press Ctrl+C to stop.")
    if len(new_descriptor.items) != 0:
        device.set_descriptor(new_descriptor)
    try:
        while True:
            report = bytearray(device.read_input_report_raw())
        #   tu je možné meniť dáta/formát reportu pred jeho spracovaním
        #   print(f"Raw report: {report.hex()}")
            device.process_input_report(report)
    except (KeyboardInterrupt, OSError):
        device.stop()
        print("\nExiting.")

if __name__ == "__main__":
    main()
