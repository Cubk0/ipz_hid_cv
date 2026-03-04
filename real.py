from ipz_hid.linux.HID_linux_device import *
from ipz_hid.core.HID_usages import *

new_descriptor: HIDDescriptor = HIDDescriptor([
#sem skopírujte upravený deskriptor s predošlej úlohy
])

def main():
    options = HIDLinuxDeviceOptions(
        attach_hidraw=True,
        make_virtual_device=True,
        grab_events=True,
    )

    device = HIDLinuxDevice.from_device_name("Keyboard", options)
    descriptor = device.get_descriptor()
    device.start()
    print("Attached to device. Press Ctrl+C to stop.")
    if len(new_descriptor.items) != 0:
        device.set_descriptor(new_descriptor)
    try:
        while True:
            report = bytearray(device.read_input_report_raw())
            print(f"Raw report: {report.hex()}")
            device.process_input_report(report)
    except (KeyboardInterrupt, OSError):
        device.stop()
        print("\nExiting.")

if __name__ == "__main__":
    main()
