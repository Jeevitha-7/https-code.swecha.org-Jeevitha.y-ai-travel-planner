import json
import os


def load_language(lang):
    current_dir = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(current_dir, "locales", f"{lang}.json")

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
