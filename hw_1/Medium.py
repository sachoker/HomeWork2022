import ast
import networkx

with open("Easy.py") as source:
    tree = ast.parse(source.read())
    dump = ast.dump(tree)

print(dump)