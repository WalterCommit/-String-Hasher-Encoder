#!/usr/bin/env python3
"""
hasher.py - String Hash & Encode CLI Tool
Original: github.com/bl4de
Updated: 2026-08-12 (Windows ANSI fix + hex_encode fix + double-click support)
"""

import sys
import os
import hashlib
import base64
import binascii
from urllib.parse import quote_plus

# Windows 10+ ANSI renk desteğini aktif et
if sys.platform == 'win32':
    os.system('')  # ANSI escape processing'i etkinleştirir

# Renk desteği
COLORS = {
    "WHITE": '\033[37m',
    "GREEN": '\033[32m',
    "CYAN": '\033[36m',
    "GREY": '\033[90m',
} if sys.stdout.isatty() else {k: "" for k in ["WHITE", "GREEN", "CYAN", "GREY"]}

ALGORITHMS = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'blake2s', 'blake2b']


def hex_encode(data: bytes) -> str:
    """Orijinal koddaki hatalı hex_encode yerine doğru implementasyon."""
    return binascii.hexlify(data).decode('ascii')


def main(s: str) -> None:
    encoded = s.encode('utf-8')

    print(f"\n{COLORS['GREEN']}HASHES:{COLORS['WHITE']}")
    for algo in ALGORITHMS:
        if hasattr(hashlib, algo):
            try:
                h = getattr(hashlib, algo)(encoded).hexdigest()
                print(f"{COLORS['GREY']}{algo:<16}\t{COLORS['CYAN']}{h}")
            except (TypeError, ValueError):
                pass

    print(f"\n{COLORS['GREEN']}ENCODE:{COLORS['WHITE']}")
    print(f"{COLORS['GREY']}Base64          \t{COLORS['CYAN']}{base64.b64encode(encoded).decode('ascii')}")
    print(f"{COLORS['GREY']}HEX encoded     \t{COLORS['CYAN']}{hex_encode(encoded)}")
    print(f"{COLORS['GREY']}URL encoded     \t{COLORS['CYAN']}{quote_plus(s)}")
    print()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("hasher.py - String Hash & Encode Tool")
        print("-" * 40)
        try:
            user_input = input("Hashlenecek metni girin: ")
            if user_input:
                main(user_input)
            else:
                print("[-] Boş girdi.")
        except (EOFError, KeyboardInterrupt):
            print("\nÇıkış.")

    # Çift tıklama desteği: terminal kapanmasın
    if not sys.stdin.isatty() or len(sys.argv) != 2:
        try:
            input("\nDevam etmek için Enter'a basın...")
        except EOFError:
            pass