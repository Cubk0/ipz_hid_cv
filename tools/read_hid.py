#!/usr/bin/env python3
import sys
import os
import termios
import tty
import signal
import select

running = True

def handle_sigint(signum, frame):
    global running
    running = False

def main():
    if len(sys.argv) != 2:
        print(f"Invalid argument :P")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
    except ValueError:
        print(f"Invalid argument :P")
        sys.exit(1)

    dev_path = f"/dev/hidraw{num}"

    if not os.path.exists(dev_path):
        print(f"Invalid file")
        sys.exit(1)

    fd_stdin = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd_stdin)
    signal.signal(signal.SIGINT, handle_sigint)

    try:
        new_settings = termios.tcgetattr(fd_stdin)
        new_settings[3] &= ~termios.ECHO
        termios.tcsetattr(fd_stdin, termios.TCSADRAIN, new_settings)

        with open(dev_path, "rb", buffering=0) as f:
            while running:
                rlist, _, _ = select.select([f], [], [], 0.1)
                if rlist:
                    data = f.read(64)
                    if data:
                        print(" ".join(f"{b:02X}" for b in data), flush=True)

    except PermissionError:
        print(f"Root needed")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        termios.tcsetattr(fd_stdin, termios.TCSADRAIN, old_settings)
        print("\nExiting.", flush=True)

if __name__ == "__main__":
    main()

