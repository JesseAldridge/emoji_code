import ast
import astor


example = """
def fake(x):
    y = ['useless list']
    return x
"""

tree = ast.parse(example)

# iterating through list which is represents function on ast
for ind, item in enumerate(tree.body[0].body):
    if isinstance(item, ast.Assign) and isinstance(item.value, ast.List):
        del tree.body[0].body[ind]
        break

print(astor.to_source(tree))
