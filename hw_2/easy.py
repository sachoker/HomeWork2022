import os

def document_gen(generator):
    def inner(*args, **kwargs):
        body = generator(*args, **kwargs)
        res = r'\documentclass{article}' + '\n' + r'\begin{document}' + '\n' + body + r'\end{document}'
        return res

    return inner


def table_gen(generator):
    def inner(*args, **kwargs):
        items = generator(*args, **kwargs)
        table = r'\begin{table}' + '\n' + r'\centering' + '\n' + r'\begin{tabular}{l|r}' + '\n'
        table += items
        table += r'\end{tabular}' + '\n' + r'\caption{\label{tab:widgets}Your table.}' + '\n' + r'\end{table}' + '\n'
        return table

    return inner


@document_gen
@table_gen
def items_gen(items: list):
    result = ''
    for item in items:
        result += fr'{item[0]} & {item[1]} \\' + '\n'
    return result


n = int(input("Введите количество строк таблицы\n"))
ls = []
for i in range(n):
    ls.append(tuple(input().split()))

with open(os.getcwd() + '/artifacts/easy.tex', 'w') as file:
    file.write(items_gen(ls))
    file.close()
