"""The Long Roast: Lawmakers — entry for make.fun.

Writes one line to /output/entry.txt.
The line is one satirical sentence about lawmakers, at most 320 characters.
"""
import os

LINE = "They want to regulate AI, crypto, and the entire internet, but ask them to convert a file to PDF and suddenly the hearing is adjourned until further notice."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
