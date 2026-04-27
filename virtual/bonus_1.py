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
    return new_report


# Úloha 2: Zablokujte klávesu A.
# Ak je kláves A stlačený, zmeňte ho na 0. Ostatné klávesy a modifikátory ponechajte nezmenené.
def zablokuj_a(report: bytearray) -> bytearray:
    new_report = bytearray(report)
    return new_report


# Úloha 3: Zmeňte kláves C na D.
# Neriešte duplicitné stlačenie (ak sa D už v reporte nachádza nechajte ho tam) 
def c_na_d(report: bytearray) -> bytearray:
    new_report = bytearray(report)
    return new_report


# Úloha 4: Zablokujte všetky modifikátory.
def odstran_modifikatory(report: bytearray) -> bytearray:
    new_report = bytearray(report)
    return new_report


# Úloha 5: Vymeňte ľavý shift a pravý shift.
# bit 1 = ľavý shift, bit 5 = pravý shift
def vymena_shiftov(report: bytearray) -> bytearray:
    new_report = bytearray(report)
    return new_report


# Úloha 6: Urobte z každého písmena veľké písmeno.
# To znamená, že ak je stlačená aspoň jedna klávesa, nastavte ľavý shift.
def vzdy_shift(report: bytearray) -> bytearray:
    new_report = bytearray(report)
    return new_report


# Úloha 7: Zmeňte číslice 1, 2, 3 na F1, F2, F3.
# Usages sú KeyboardUsage.NUMBER_1,.., KeyboardUsage.F1,..
def cisla_na_funkcne(report: bytearray) -> bytearray:
    new_report = bytearray(report)
    return new_report


# Úloha 8: Zablokujte kombináciu Ctrl+C.
# bit 0 = Left Ctrl, bit 4 = Right Ctrl, kláves C = KeyboardUsage.C
def blokuj_ctrl_c(report: bytearray) -> bytearray:
    new_report = bytearray(report)
    return new_report


# Úloha 9: Premeňte klávesu Q na kombináciu Ctrl+Q.
def q_na_ctrl_q(report: bytearray) -> bytearray:
    new_report = bytearray(report)
    return new_report


