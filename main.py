from pathlib import Path
import sys
from typing import Dict
from typing import List

from stats import count_chars
from stats import get_n_words
from stats import sort_dict


# ============================================
#                 get_book_text
# ============================================
def get_book_text(fPath: Path) -> str:
    with open(fPath, "r", encoding="utf-8") as fd:
        fContents: str = fd.read()
    return fContents


# ============================================
#                 print_report
# ============================================
def print_report(numWords: int, sortedChars: List[Dict], bookName: str) -> None:
    header: str = "=" * 11 + " BOOKBOT " + "=" * 11
    print(header)
    print("Analyzing book found at books/frankenstein.txt...")
    header = "-" * 11 + " Word Count " + "-" * 11
    print(header)
    print(f"Found {numWords} total words")
    header = "-" * 9 + " Character Count " + "-" * 7
    print(header)

    for d in sortedChars:
        print(f"{d['char']}: {d['num']}")


# ============================================
#                     main
# ============================================
def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    contents: str = get_book_text(Path(sys.argv[1]))
    numWords: int = get_n_words(contents)
    nChars: Dict[str, int] = count_chars(contents)
    sortedChars: List[Dict] = sort_dict(nChars)

    print_report(numWords, sortedChars, sys.argv[1])

    return 0


if __name__ == "__main__":
    main()
