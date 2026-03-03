from ipz_hid.core.HID_classes import HIDDescriptor
from ipz_hid.linux.HID_linux_device import HIDLinuxDevice, HIDLinuxDeviceOptions
from ipz_hid.core.HID_usages import *
from ipz_hid.core.HID_items import *
from uloha_1 import vymena_klaves


descriptor = HIDDescriptor([
    UsagePageItem(UsagePage.GENERIC_DESKTOP),
    UsageItem(GenericDesktopUsage.KEYBOARD),
    CollectionItem(HIDCollectionType.APPLICATION),

    # Modifier byte
    ReportSizeItem(1),
    ReportCountItem(8),
    UsagePageItem(UsagePage.KEYBOARD_KEYPAD),
    UsageMinimumItem(224),
    UsageMaximumItem(231),
    LogicalMinItem(0),
    LogicalMaxItem(1),
    InputItem(HIDFieldAttributes(is_variable=True)),

    # Reserved byte
    ReportCountItem(1),
    ReportSizeItem(8),
    InputItem(HIDFieldAttributes(is_constant=True)),

    # LED output report (5 bits)
    ReportCountItem(5),
    ReportSizeItem(1),
    UsagePageItem(UsagePage.LEDS),
    UsageMinimumItem(1),
    UsageMaximumItem(5),
    OutputItem(HIDFieldAttributes(is_variable=True)),

    # LED report padding (3 bits)
    ReportCountItem(1),
    ReportSizeItem(3),
    OutputItem(HIDFieldAttributes(is_constant=True)),

    # Key array (6 bytes)
    ReportCountItem(6),
    ReportSizeItem(8),
    UsagePageItem(UsagePage.KEYBOARD_KEYPAD),
    UsageMinimumItem(0),
    UsageMaximumItem(255),
    LogicalMinItem(0),
    LogicalMaxItem(255),
    InputItem(HIDFieldAttributes(is_variable=False)),

    EndCollectionItem()
])

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def test_vymena_klaves():
    tests = [
        (bytearray([0b00000101,0x0, KeyboardUsage.B, KeyboardUsage.A,0x0,0x0,0x0,0x0]), bytearray([0b00000101,0x0, KeyboardUsage.A, KeyboardUsage.B, 0x0, 0x0, 0x0, 0x0]), "A and B swapped"),
        (bytearray([0b00000111,0x0, KeyboardUsage.C, KeyboardUsage.B, KeyboardUsage.A,0x0,0x0,0x0]), bytearray([0b00000111,0x0,KeyboardUsage.C, KeyboardUsage.A, KeyboardUsage.B, 0x0, 0x0, 0x0]), "A and B swapped not first index"),
        (bytearray([0b00000101,0x0, KeyboardUsage.C, KeyboardUsage.D,0x0,0x0,0x0,0x0]), bytearray([0b00000101,0x0, KeyboardUsage.C, KeyboardUsage.D, 0x0, 0x0, 0x0, 0x0]), "No change needed"),
    ]
    passed = 0
    for i, (report, expected, desc) in enumerate(tests):
        result = vymena_klaves(report)
        if result != expected:
            print(f"{RED}[vymena_klaves] Test {i} failed ({desc}):\n got {result}\n expected {expected}{RESET}")
        else:
            print(f"{GREEN}[vymena_klaves] Test {i} passed ({desc}){RESET}")
            passed += 1
    return passed, len(tests)

if __name__ == "__main__":
    s1_passed, s1_total = test_vymena_klaves()

    total_passed = s1_passed

    print(f"\n{YELLOW}Summary: Passed {total_passed}/{s1_total} tests{RESET}")
    if total_passed == s1_total:
        print(f"{GREEN}All tests passed!{RESET}")
    else:
        print(f"{RED}Some tests failed. Check above messages for details.{RESET}")
