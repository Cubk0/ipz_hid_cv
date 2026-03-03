#!/usr/bin/env python
import glob, os

for dev in glob.glob("/sys/class/hidraw/hidraw*"):
    node = "/dev/" + os.path.basename(dev)
    uevent = os.path.join(dev, "device/uevent")
    vendor = product = name = None

    if os.path.exists(uevent):
        with open(uevent) as f:
            for line in f:
                if line.startswith("HID_NAME="):
                    name = line.strip().split("=", 1)[1]
                if line.startswith("HID_ID="):
                    _, ids = line.strip().split("=")
                    bus, vid, pid = ids.split(":")
                    vendor, product = vid, pid

    print(f"{node} -> {name or 'Unknown'} (Vendor={vendor}, Product={product})")

