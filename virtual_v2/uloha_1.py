from ipz_hid.core.HID_classes import HIDDescriptor
from ipz_hid.core.HID_items import *
from ipz_hid.core.HID_usages import *

# neupravený deskriptor
descriptor = HIDDescriptor([
    UsagePageItem(UsagePage.GENERIC_DESKTOP),
    UsageItem(GenericDesktopUsage.KEYBOARD),
    CollectionItem(HIDCollectionType.APPLICATION),

    # 0-9
    UsagePageItem(UsagePage.KEYBOARD_KEYPAD),
    ReportSizeItem(1),
    ReportCountItem(10),
    LogicalMinItem(0),
    LogicalMaxItem(1),
    UsageMinimumItem(KeyboardUsage.NUMBER_1),
    UsageMaximumItem(KeyboardUsage.NUMBER_0),
    InputItem(HIDFieldAttributes(is_variable=True)),
    # A and B
    ReportSizeItem(1),
    ReportCountItem(2),
    LogicalMinItem(0),
    LogicalMaxItem(1),
    UsageItem(KeyboardUsage.A),
    UsageItem(KeyboardUsage.B),
    InputItem(HIDFieldAttributes(is_variable=True)),
    # Padding
    ReportSizeItem(4),
    ReportCountItem(1),
    InputItem(HIDFieldAttributes(is_constant=True)),
    EndCollectionItem()
])

# Úlohy na zmenu výzmamu HID upravením deskriptoru.
# V týchto úlohách budeme meniť report descriptor z klávesnice.Descriptor opisuje 16 bitov (2 bajty): 
# - bity 0-9 reprezentujú čísla 1-0 (1,2,3,4,5,6,7,8,9,0), 
# - bity 10-11 reprezentujú klávesy A a B, 
# - bity 12-15 sú padding.
# Opis vo forme bajtov:
# - bajt 0: bity 0-7 reprezentujú čísla 1-8 
# - bajt 1: bity 0 a 1 reprezentujú čísla 9 a 0, bity 2 a 3 reprezentujú klávesy A a B, ostatné bity sú padding 



# Úloha 1: Upravte descriptor_1 tak, aby boli klávesy A a B vymenené.
descriptor_1 = HIDDescriptor([
    UsagePageItem(UsagePage.GENERIC_DESKTOP),
    UsageItem(GenericDesktopUsage.KEYBOARD),
    CollectionItem(HIDCollectionType.APPLICATION),

    # 0-9
    UsagePageItem(UsagePage.KEYBOARD_KEYPAD),
    ReportSizeItem(1),
    ReportCountItem(10),
    LogicalMinItem(0),
    LogicalMaxItem(1),
    UsageMinimumItem(KeyboardUsage.NUMBER_1),
    UsageMaximumItem(KeyboardUsage.NUMBER_0),
    InputItem(HIDFieldAttributes(is_variable=True)),
    # A and B
    ReportSizeItem(1),
    ReportCountItem(2),
    LogicalMinItem(0),
    LogicalMaxItem(1),
    UsageItem(KeyboardUsage.A),
    UsageItem(KeyboardUsage.B),
    InputItem(HIDFieldAttributes(is_variable=True)),
    # Padding
    ReportSizeItem(4),
    ReportCountItem(1),
    InputItem(HIDFieldAttributes(is_constant=True)),
    EndCollectionItem()
])
def vymena_klaves()->HIDDescriptor:
  return descriptor_1
