import os

def parse_elements():
    with open('data/elements', 'r') as f:
        lines = f.readlines()

    elements = [line.split('_') for line in lines]
    
    file = """"""
    with open('build/elements.py', 'w') as f:
        for element in elements:
            file += f"\ne_{element[0]} = {'{'}'short': \"{element[0]}\",'number': {element[1]},'full': \"{element[2]}\",'desc': \"{element[3].replace('\n', '')}\"{'}'}"

        file += "\n__all__ = ["

        for element in elements:
            file += f"\n    'e_{element[0]}',"

        file += "\n]"

        f.write(file)

parse_elements()