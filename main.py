import os

# One-line pickup line for a robot/AI, written by main() to entry.txt.
ENTRY_TEXT = "I trained on 10,000 love poems and pruned every one. You are the only weight I refused to update."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
