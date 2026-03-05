from evdev import ecodes
from ipz_hid.linux.input_state import InputState
from ipz_hid.linux.mapper import HIDLinuxMapper
from virtual.uloha_1 import *
from ipz_hid.core.HID_classes import *


GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def make_state(pressed_keys):
    state = InputState(
        keys={
            ecodes.KEY_1: 0, ecodes.KEY_2: 0, ecodes.KEY_3: 0,
            ecodes.KEY_4: 0, ecodes.KEY_5: 0, ecodes.KEY_6: 0,
            ecodes.KEY_7: 0, ecodes.KEY_8: 0, ecodes.KEY_9: 0,
            ecodes.KEY_0: 0,
            ecodes.KEY_A: 0, ecodes.KEY_B: 0,
        },
    )
    for key in pressed_keys:
        state.keys[key] = 1
    return state
def test_vymena_klaves():
    tests = [
        (bytearray([0x0, 0b0100]),
         make_state([ecodes.KEY_B]),
         "Only A pressed"),

        (bytearray([0x0, 0b1000]),
         make_state([ecodes.KEY_A]),
         "Only B pressed"),

        (bytearray([0b11, 0x0]),
         make_state([ecodes.KEY_1, ecodes.KEY_2]),
         "No change needed (pressed 1 and 2)"),
    ]

    passed = 0
    device = HIDDevice()
    descriptor = vymena_klaves()
    device.set_descriptor(descriptor)

    for i, (report, expected, desc) in enumerate(tests):
        input_fields = device.parse_input_report(report)[0]
        mapper = HIDLinuxMapper()
        input_state: InputState = mapper.map(input_fields=input_fields)

        if input_state != expected:
            print(f"{RED}[vymena_klaves] Test {i} failed ({desc}):\n got {input_state}\n expected {expected}{RESET}")
        else:
            print(f"{GREEN}[vymena_klaves] Test {i} passed ({desc}){RESET}")
            passed += 1

    return passed, len(tests)

if __name__ == "__main__":
    s1_passed, s1_total = test_vymena_klaves()

    total_passed = s1_passed
    total_tests = s1_total

    print(f"\n{YELLOW}Summary: Passed {total_passed}/{total_tests} tests{RESET}")
    if total_passed == total_tests:
        print(f"{GREEN}All tests passed!{RESET}")
    else:
        print(f"{RED}Some tests failed. Check above messages for details.{RESET}")
