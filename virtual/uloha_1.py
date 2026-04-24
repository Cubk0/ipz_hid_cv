from ipz_hid.core.HID_classes import HIDDescriptor
from ipz_hid.core.HID_items import *
from ipz_hid.core.HID_usages import *

# neupravený deskriptor
# tento deskriptor neupravujte úloha je nižšie
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
    # A a B
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

# Layout klávesnice:
# 1 2 3
# 4 5 6
# 7 8 9
# A 0 B

# Úlohy na zmenu výzmamu HID upravením deskriptoru.
# V týchto úlohách budeme meniť report descriptor z klávesnice.Descriptor opisuje 16 bitov (2 bajty): 
# - bity 0-9 reprezentujú čísla 1-0 (1,2,3,4,5,6,7,8,9,0 v tomto poradí), 
# - bity 10-11 reprezentujú klávesy A a B, 
# - bity 12-15 sú padding.



# Úloha 1: Upravte descriptor_1 tak, aby boli klávesy A a B vymenené.
# Nemente formát reportu, len význam jednotlivých bitov. Po úprave by mal bit 10 reprezentovat klávesu B a bit 11 klávesu A.
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
    # A a B
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
