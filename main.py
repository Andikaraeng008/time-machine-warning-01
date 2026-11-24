import os

TEXT = "WARNING: Do not meet your earlier self. He has already filed a complaint about you."

def main():
    assert 1 <= len(TEXT) <= 120 and TEXT.strip(), "gate: 1-120 chars, not whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
