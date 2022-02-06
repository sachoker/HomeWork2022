import os


def generate_document(generator):
    def inner(*args, **kwargs):
        body = generator(*args, **kwargs)
        image = r'''\usepackage{graphicx}
\graphicspath{{/}}
\DeclareGraphicsExtensions{.pdf,.png,.jpg}
'''
        res = r'\documentclass{article}' + '\n' + image + r'\begin{document}' + '\n' + body + r'\end{document}'
        return res

    return inner


def table_gen(generator):
    def inner(*args, **kwargs):
        items = generator(*args, **kwargs)
        global lines
        try:
            table = r'\begin{table}' + '\n' + r'\centering' + '\n' + r'\begin{tabular}{' + '|' + "l|"*lines + '}' + '\n'
        except NameError:
            table = r'\begin{table}' + '\n' + r'\centering' + '\n' + r'\begin{tabular}{l | l}' + '\n'
        table += items
        table += r'\end{tabular}' + '\n' + r'\caption{\label{tab:widgets}Your table.}' + '\n' + r'\end{table}' + '\n'
        return table

    return inner


@generate_document
@table_gen
def items_gen(items: list):
    result = ''
    for item in items:
        temp = ''
        for i in item[:-1]:
            temp += f'{i} & '
        # result += fr'{item[0]} & {item[1]} \\' + '\n'
        temp += fr'{item[-1]} \\' + '\n'
        result += temp
    return result


@table_gen
def generate_items():
    items = [('Wood', 25), ('Rock', 100), ('Oil', 10), ('Workers', 5)]
    result = ''
    for item in items:
        result += fr'{item[0]} & {item[1]} \\' + '\n'
    return result


if __name__ == '__main__':
    lines = int(input('Введите количество строк\n'))
    n = int(input("Введите количество строк таблицы\n"))
    ls = []
    for i in range(n):
        ls.append(tuple(input().split()))

    with open(os.getcwd() + '/artifacts/easy.tex', 'w') as file:
        #file.write(generate_items())
        file.write(items_gen(ls))
        file.close()
