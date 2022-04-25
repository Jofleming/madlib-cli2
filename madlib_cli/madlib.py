import re

def welcome_message():
    print('Welcome! This is a game of madlibs. Input words that match the prompt.')

def read_template(file):
    with open(file, "r") as line_template:
        return line_template.read()

def parse_template(line_template):
    pattern = r"\{(\w+\s*\w+\s*\w+\s*\w+)\}"
    actual_stripped = re.sub(pattern,"{}", line_template)
    actual_parts = tuple(re.findall(pattern, line_template))
    return (actual_stripped, actual_parts)

def merge(stripped_template, users_words):
    finished_madlib = stripped_template.format(*users_words)
    return finished_madlib