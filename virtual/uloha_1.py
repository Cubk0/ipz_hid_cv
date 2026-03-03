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



#  Úloha 1: Zmeňte report tak, aby boli klávesy A a B vymenené.
def vymena_klaves(report: bytearray)->bytearray:
    # Referenčné riešenie
    new_report = bytearray(report)
    # Vymeníme klávesy A (0x1E) a B (0x30)
    for i in range(2, 8):
        if new_report[i] == KeyboardUsage.A:
            new_report[i] = KeyboardUsage.B
        elif new_report[i] == KeyboardUsage.B:
            new_report[i] = KeyboardUsage.A
    return new_report



