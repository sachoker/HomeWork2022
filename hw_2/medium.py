import subprocess
import os
from imagegen.graphgen import generate_image

from easy import generate_document, generate_items


def generate_latex_img(img: str):
    return r'\includegraphics' + '{' + img + '}' + '\n'


@generate_document
def concate_body(*args):
    res = ''
    for string in args:
        res += string
    return res


if __name__ == '__main__':
    generate_image()
    with open(os.getcwd() + '/artifacts/medium.tex', 'w') as file:
        file.write(concate_body(generate_items(), generate_latex_img('Graph')))
        subprocess.run(r'cd .\artifacts')
        subprocess.call('pdflatex medium')
        file.close()
