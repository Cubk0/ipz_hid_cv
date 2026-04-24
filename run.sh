#!/usr/bin/env bash
set -euo pipefail

cleanup() {
    trap - INT TERM
    kill -- -$$ 2>/dev/null || true
    wait || true
    exit 130
}

trap cleanup INT TERM

(
    # Skript pre spustenie real.py ktorý upravý spracovanie HID správ
    exec sudo python3 ~/cvicenie/real.py
) &

(
    # Sem pridajte spustenie vášho skriptu, napríklad:
    # exec sudo ~/projekt/.venv/bin/python script.py
) &

wait