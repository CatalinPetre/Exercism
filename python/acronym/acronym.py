import re


def abbreviate(words):
    sep = r'_|\s|-'
    words = re.split(sep, words)
    acronym = [pattern[0] for pattern in words if pattern]
    return "".join(acronym).upper()
