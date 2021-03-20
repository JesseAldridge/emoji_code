import ast, re

import astor, emojis


text = '''
def _emoji_satisfied_emoji_():
  return f"_emoji_satisfied_emoji_ {'_emoji_ghost_emoji_' + _emoji_ghost_emoji_() + '_emoji_ghost_emoji_'} _emoji_satisfied_emoji_"

def _emoji_ghost_emoji_():
  return ".~.*._emoji_ghost_emoji_.*.~."

'''

tree = ast.parse(text)

print('dump:', ast.dump(tree, indent=2))

class ConstantToEmoji(ast.NodeTransformer):
  def visit_Constant(self, node):
    node.value = emojis.encode(re.sub('_emoji_([a-z]+)_emoji_', ':\g<1>:', node.value))
    return node

tree = ConstantToEmoji().visit(tree)

print('rewritten:', astor.to_source(tree))
