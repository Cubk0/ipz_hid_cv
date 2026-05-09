from ipz_hid.core.descriptor import HIDDescriptor
from ipz_hid.linux.hid_linux_device import HIDLinuxDevice, HIDLinuxDeviceOptions
from ipz_hid.core.hid_usages import *
from ipz_hid.core.hid_items import *
from bonus_1 import (
    vymena_klaves,
    zablokuj_a,
    c_na_d,
    odstran_modifikatory,
    vymena_shiftov,
    vzdy_shift,
    cisla_na_funkcne,
    blokuj_ctrl_c,
    q_na_ctrl_q
)

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
        (bytearray([0b00000101, 0x0, KeyboardUsage.B, KeyboardUsage.A, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00000101, 0x0, KeyboardUsage.A, KeyboardUsage.B, 0x0, 0x0, 0x0, 0x0]),
         "A and B swapped"),

        (bytearray([0b00000111, 0x0, KeyboardUsage.C, KeyboardUsage.B, KeyboardUsage.A, 0x0, 0x0, 0x0]),
         bytearray([0b00000111, 0x0, KeyboardUsage.C, KeyboardUsage.A, KeyboardUsage.B, 0x0, 0x0, 0x0]),
         "A and B swapped not first index"),

        (bytearray([0b00000101, 0x0, KeyboardUsage.C, KeyboardUsage.D, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00000101, 0x0, KeyboardUsage.C, KeyboardUsage.D, 0x0, 0x0, 0x0, 0x0]),
         "No change needed"),
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


def test_zablokuj_a():
    tests = [
        (bytearray([0b00000000, 0x0, KeyboardUsage.A, KeyboardUsage.B, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00000000, 0x0, 0x0, KeyboardUsage.B, 0x0, 0x0, 0x0, 0x0]),
         "A removed"),

        (bytearray([0b00000000, 0x0, KeyboardUsage.C, KeyboardUsage.D, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00000000, 0x0, KeyboardUsage.C, KeyboardUsage.D, 0x0, 0x0, 0x0, 0x0]),
         "No A present"),

        (bytearray([0b00000000, 0x0, KeyboardUsage.A, KeyboardUsage.A, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00000000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]),
         "Multiple A removed"),
    ]
    passed = 0
    for i, (report, expected, desc) in enumerate(tests):
        result = zablokuj_a(report)
        if result != expected:
            print(f"{RED}[zablokuj_a] Test {i} failed ({desc}):\n got {result}\n expected {expected}{RESET}")
        else:
            print(f"{GREEN}[zablokuj_a] Test {i} passed ({desc}){RESET}")
            passed += 1
    return passed, len(tests)


def test_c_na_d():
    tests = [
        (bytearray([0b00000000, 0x0, KeyboardUsage.C, 0x0, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00000000, 0x0, KeyboardUsage.D, 0x0, 0x0, 0x0, 0x0, 0x0]),
         "C replaced with D"),

        (bytearray([0b00000000, 0x0, KeyboardUsage.A, KeyboardUsage.B, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00000000, 0x0, KeyboardUsage.A, KeyboardUsage.B, 0x0, 0x0, 0x0, 0x0]),
         "No C present"),

        (bytearray([0b00000000, 0x0, KeyboardUsage.C, KeyboardUsage.C, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00000000, 0x0, KeyboardUsage.D, KeyboardUsage.D, 0x0, 0x0, 0x0, 0x0]),
         "Multiple C replaced"),
    ]
    passed = 0
    for i, (report, expected, desc) in enumerate(tests):
        result = c_na_d(report)
        if result != expected:
            print(f"{RED}[c_na_d] Test {i} failed ({desc}):\n got {result}\n expected {expected}{RESET}")
        else:
            print(f"{GREEN}[c_na_d] Test {i} passed ({desc}){RESET}")
            passed += 1
    return passed, len(tests)


def test_odstran_modifikatory():
    tests = [
        (bytearray([0b11111111, 0x0, KeyboardUsage.A, 0x0, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00000000, 0x0, KeyboardUsage.A, 0x0, 0x0, 0x0, 0x0, 0x0]),
         "All modifiers removed"),

        (bytearray([0b00000000, 0x0, KeyboardUsage.B, 0x0, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00000000, 0x0, KeyboardUsage.B, 0x0, 0x0, 0x0, 0x0, 0x0]),
         "Already no modifiers"),

        (bytearray([0b00010001, 0x0, KeyboardUsage.C, KeyboardUsage.D, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00000000, 0x0, KeyboardUsage.C, KeyboardUsage.D, 0x0, 0x0, 0x0, 0x0]),
         "Only modifiers changed"),
    ]
    passed = 0
    for i, (report, expected, desc) in enumerate(tests):
        result = odstran_modifikatory(report)
        if result != expected:
            print(f"{RED}[odstran_modifikatory] Test {i} failed ({desc}):\n got {result}\n expected {expected}{RESET}")
        else:
            print(f"{GREEN}[odstran_modifikatory] Test {i} passed ({desc}){RESET}")
            passed += 1
    return passed, len(tests)


def test_vymena_shiftov():
    tests = [
        (bytearray([0b00000010, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00100000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]),
         "Left Shift changed to Right Shift"),

        (bytearray([0b00100000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00000010, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]),
         "Right Shift changed to Left Shift"),

        (bytearray([0b00100010, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00100010, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]),
         "Both shifts stay pressed"),
    ]
    passed = 0
    for i, (report, expected, desc) in enumerate(tests):
        result = vymena_shiftov(report)
        if result != expected:
            print(f"{RED}[vymena_shiftov] Test {i} failed ({desc}):\n got {result}\n expected {expected}{RESET}")
        else:
            print(f"{GREEN}[vymena_shiftov] Test {i} passed ({desc}){RESET}")
            passed += 1
    return passed, len(tests)


def test_vzdy_shift():
    tests = [
        (bytearray([0b00000000, 0x0, KeyboardUsage.A, 0x0, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00000010, 0x0, KeyboardUsage.A, 0x0, 0x0, 0x0, 0x0, 0x0]),
         "Shift added when key is pressed"),

        (bytearray([0b00000000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00000000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]),
         "No key pressed"),

        (bytearray([0b00100000, 0x0, KeyboardUsage.B, 0x0, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00100010, 0x0, KeyboardUsage.B, 0x0, 0x0, 0x0, 0x0, 0x0]),
         "Left Shift added while preserving other modifiers"),
    ]
    passed = 0
    for i, (report, expected, desc) in enumerate(tests):
        result = vzdy_shift(report)
        if result != expected:
            print(f"{RED}[vzdy_shift] Test {i} failed ({desc}):\n got {result}\n expected {expected}{RESET}")
        else:
            print(f"{GREEN}[vzdy_shift] Test {i} passed ({desc}){RESET}")
            passed += 1
    return passed, len(tests)


def test_cisla_na_funkcne():
    tests = [
        (bytearray([0b00000000, 0x0, KeyboardUsage.NUMBER_1, KeyboardUsage.NUMBER_2, KeyboardUsage.NUMBER_3, 0x0, 0x0, 0x0]),
         bytearray([0b00000000, 0x0, KeyboardUsage.F1, KeyboardUsage.F2, KeyboardUsage.F3, 0x0, 0x0, 0x0]),
         "1 2 3 changed to F1 F2 F3"),

        (bytearray([0b00000000, 0x0, KeyboardUsage.A, KeyboardUsage.B, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00000000, 0x0, KeyboardUsage.A, KeyboardUsage.B, 0x0, 0x0, 0x0, 0x0]),
         "No number keys present"),

        (bytearray([0b00000000, 0x0, KeyboardUsage.NUMBER_2, 0x0, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00000000, 0x0, KeyboardUsage.F2, 0x0, 0x0, 0x0, 0x0, 0x0]),
         "Single number key changed"),
    ]
    passed = 0
    for i, (report, expected, desc) in enumerate(tests):
        result = cisla_na_funkcne(report)
        if result != expected:
            print(f"{RED}[cisla_na_funkcne] Test {i} failed ({desc}):\n got {result}\n expected {expected}{RESET}")
        else:
            print(f"{GREEN}[cisla_na_funkcne] Test {i} passed ({desc}){RESET}")
            passed += 1
    return passed, len(tests)


def test_blokuj_ctrl_c():
    tests = [
        (bytearray([0b00000001, 0x0, KeyboardUsage.C, KeyboardUsage.A, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00000001, 0x0, 0x0, KeyboardUsage.A, 0x0, 0x0, 0x0, 0x0]),
         "Left Ctrl + C blocked"),

        (bytearray([0b00010000, 0x0, KeyboardUsage.C, 0x0, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00010000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]),
         "Right Ctrl + C blocked"),

        (bytearray([0b00000000, 0x0, KeyboardUsage.C, KeyboardUsage.A, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00000000, 0x0, KeyboardUsage.C, KeyboardUsage.A, 0x0, 0x0, 0x0, 0x0]),
         "C without Ctrl allowed"),
    ]
    passed = 0
    for i, (report, expected, desc) in enumerate(tests):
        result = blokuj_ctrl_c(report)
        if result != expected:
            print(f"{RED}[blokuj_ctrl_c] Test {i} failed ({desc}):\n got {result}\n expected {expected}{RESET}")
        else:
            print(f"{GREEN}[blokuj_ctrl_c] Test {i} passed ({desc}){RESET}")
            passed += 1
    return passed, len(tests)


def test_q_na_ctrl_q():
    tests = [
        (bytearray([0b00000000, 0x0, KeyboardUsage.Q, 0x0, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00000001, 0x0, KeyboardUsage.Q, 0x0, 0x0, 0x0, 0x0, 0x0]),
         "Q changed to Ctrl+Q"),

        (bytearray([0b00010000, 0x0, KeyboardUsage.Q, 0x0, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00010001, 0x0, KeyboardUsage.Q, 0x0, 0x0, 0x0, 0x0, 0x0]),
         "Q adds Left Ctrl while preserving Right Ctrl"),

        (bytearray([0b00000000, 0x0, KeyboardUsage.W, 0x0, 0x0, 0x0, 0x0, 0x0]),
         bytearray([0b00000000, 0x0, KeyboardUsage.W, 0x0, 0x0, 0x0, 0x0, 0x0]),
         "No Q present"),
    ]
    passed = 0
    for i, (report, expected, desc) in enumerate(tests):
        result = q_na_ctrl_q(report)
        if result != expected:
            print(f"{RED}[q_na_ctrl_q] Test {i} failed ({desc}):\n got {result}\n expected {expected}{RESET}")
        else:
            print(f"{GREEN}[q_na_ctrl_q] Test {i} passed ({desc}){RESET}")
            passed += 1
    return passed, len(tests)


if __name__ == "__main__":
    s1_passed, s1_total = test_vymena_klaves()
    s2_passed, s2_total = test_zablokuj_a()
    s3_passed, s3_total = test_c_na_d()
    s4_passed, s4_total = test_odstran_modifikatory()
    s5_passed, s5_total = test_vymena_shiftov()
    s6_passed, s6_total = test_vzdy_shift()
    s7_passed, s7_total = test_cisla_na_funkcne()
    s8_passed, s8_total = test_blokuj_ctrl_c()
    s9_passed, s9_total = test_q_na_ctrl_q()

    total_passed = (
        s1_passed + s2_passed + s3_passed + s4_passed +
        s5_passed + s6_passed + s7_passed + s8_passed + s9_passed
    )
    total_tests = (
        s1_total + s2_total + s3_total + s4_total +
        s5_total + s6_total + s7_total + s8_total + s9_total
    )

    print(f"\n{YELLOW}Summary: Passed {total_passed}/{total_tests} tests{RESET}")
    if total_passed == total_tests:
        print(f"{GREEN}All tests passed!{RESET}")
    else:
        print(f"{RED}Some tests failed. Check above messages for details.{RESET}")