"""Write one funny single-line developer excuse for a production outage."""

import os

ENTRY = "The fix never reached production \u2014 it's on my laptop at home, updating, with 4% battery and the lid closed."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
