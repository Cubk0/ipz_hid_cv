from ipz_hid.linux.HID_linux_device import *
from ipz_hid.core.HID_usages import *
from ipz_hid.core.HID_items import *

# !!! Deskriptor neupravovať !!!
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
# !!! Deskriptor neupravovať !!!


# Úlohy na zmenu výzmamu HID upravením vstupného reportu.
# 
# V týchto úlohách budeme meniť report z klávesnice (celý deskriptor je vyšie). Report má 8 bajtov:
# - bajt 0: bity 0-7 reprezentujú modifikátory (Ctrl, Shift, Alt, GUI, ...)
# - bajt 1: reserved (nepoužíva sa a vždy je 0)
# - bajt 2-7: reprezentujú stlačené klávesy (0 ak žiadna klávesa nie je stlačená, inak kód stlačenej klávesy)


# Úloha 1: Zmeňte report tak, aby boli klávesy A a B vymenené.
def vymena_klaves(report: bytearray) -> bytearray:
    new_report = bytearray(report)
    for i in range(2, 8):
        if new_report[i] == KeyboardUsage.A:
            new_report[i] = KeyboardUsage.B
        elif new_report[i] == KeyboardUsage.B:
            new_report[i] = KeyboardUsage.A
    return new_report


# Úloha 2: Zablokujte kláves A.
# Ak je kláves A stlačený, zmeňte ho na 0. Ostatné klávesy a modifikátory ponechajte nezmenené.
def zablokuj_a(report: bytearray) -> bytearray:
    new_report = bytearray(report)
    for i in range(2, 8):
        if new_report[i] == KeyboardUsage.A:
            new_report[i] = 0
    return new_report


# Úloha 3: Zmeňte kláves C na D.
def c_na_d(report: bytearray) -> bytearray:
    new_report = bytearray(report)
    for i in range(2, 8):
        if new_report[i] == KeyboardUsage.C:
            new_report[i] = KeyboardUsage.D
    return new_report


# Úloha 4: Zablokujte všetky modifikátory.
def odstran_modifikatory(report: bytearray) -> bytearray:
    new_report = bytearray(report)
    new_report[0] = 0
    return new_report


# Úloha 5: Vymeňte ľavý Shift a pravý Shift.
# bit 1 = Left Shift, bit 5 = Right Shift
def vymena_shiftov(report: bytearray) -> bytearray:
    new_report = bytearray(report)

    left_shift = (new_report[0] >> 1) & 1
    right_shift = (new_report[0] >> 5) & 1

    new_report[0] &= ~(1 << 1)
    new_report[0] &= ~(1 << 5)

    new_report[0] |= (left_shift << 5)
    new_report[0] |= (right_shift << 1)

    return new_report


# Úloha 6: Urobte z každého písmena veľké písmeno.
# To znamená, že ak je stlačená aspoň jedna klávesa, nastavte Left Shift.
def vzdy_shift(report: bytearray) -> bytearray:
    new_report = bytearray(report)
    if any(new_report[i] != 0 for i in range(2, 8)):
        new_report[0] |= (1 << 1)  # Left Shift
    return new_report


# Úloha 7: Zmeňte číslice 1, 2, 3 na F1, F2, F3.
# Usages sú KeyboardUsage.NUMBER_1,.., KeyboardUsage.F1,..
def cisla_na_funkcne(report: bytearray) -> bytearray:
    new_report = bytearray(report)
    for i in range(2, 8):
        if new_report[i] == KeyboardUsage.NUMBER_1:
            new_report[i] = KeyboardUsage.F1
        elif new_report[i] == KeyboardUsage.NUMBER_2:
            new_report[i] = KeyboardUsage.F2
        elif new_report[i] == KeyboardUsage.NUMBER_3:
            new_report[i] = KeyboardUsage.F3
    return new_report


# Úloha 8: Zablokujte kombináciu Ctrl+C.
# bit 0 = Left Ctrl, bit 4 = Right Ctrl, kláves C = KeyboardUsage.C
def blokuj_ctrl_c(report: bytearray) -> bytearray:
    new_report = bytearray(report)
    left_ctrl = (new_report[0] >> 0) & 1
    right_ctrl = (new_report[0] >> 4) & 1

    if left_ctrl or right_ctrl:
        for i in range(2, 8):
            if new_report[i] == KeyboardUsage.C:
                new_report[i] = 0

    return new_report


# Úloha 9: Premeňte kláves Q na kombináciu Ctrl+Q.
def q_na_ctrl_q(report: bytearray) -> bytearray:
    new_report = bytearray(report)
    if KeyboardUsage.Q in new_report[2:8]:
        new_report[0] |= (1 << 0)  # Left Ctrl
    return new_report


