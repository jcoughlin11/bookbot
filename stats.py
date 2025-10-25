from typing import Dict
from typing import List


# ============================================
#                 get_n_words
# ============================================
def get_n_words(text: str) -> int:
    return len(text.split())


# ============================================
#                 count_chars
# ============================================
def count_chars(text: str) -> Dict[str, int]:
    results: Dict[str, int] = {}

    for char in text:
        key: str = char.lower()
        results[key] = results.setdefault(key, 0) + 1

    return results


# ============================================
#                 sort_dict
# ============================================
def sort_dict(charCounts: Dict[str, int]) -> List[Dict]:
    results = []
    for char, count in charCounts.items():
        if char.isalpha():
            results.append({"char": char, "num": count})

    def sort_on(items):
        return items["num"]

    results.sort(reverse=True, key=sort_on)

    return results
