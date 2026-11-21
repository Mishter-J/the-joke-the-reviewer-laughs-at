import os
JOKE = "I asked my agent to review its own code. It left one comment: 'LGTM \u2014 the author is very talented.'"
def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
if __name__ == "__main__":
    main()
