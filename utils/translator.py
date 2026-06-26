import json
import os


def load_language(lang):
    path = os.path.join("locales", f"{lang}.json")

    with open(path, encoding="utf-8") as file:
        return json.load(file)


def translate_text(text, _target_language):
    return text
