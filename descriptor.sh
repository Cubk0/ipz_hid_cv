cat /sys/class/hidraw/hidraw$1/device/report_descriptor | hidrd-convert -o spec
