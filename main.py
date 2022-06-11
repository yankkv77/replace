with open('text.txt', 'r', encoding="utf-8") as f:
    text = f.read()
replace_letters = {"А": "A", "а": "a", "В": "B", "С": "C", "с": "c",
                   "Е": "E", "е": "e", "К": "K", "О": "O", "о": "o", "Р": "P", "р": "p", "Х": "X", "х": "x", "Н": "H"}


def replace_text(text, replace_letters):
    if not isinstance(text, str) or text.strip().isdigit():
        return
    for k, v in replace_letters.items():
        text = text.replace(k, v)
    return text


with open('text.txt', 'w', encoding="utf-8") as f:
    f.write((
        replace_text(text, replace_letters)))
