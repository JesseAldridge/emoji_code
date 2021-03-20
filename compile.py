#!/usr/bin/env python3
import random, re, glob, os, shutil, ast

import emojis, astor


def main():
  shutil.rmtree('compiled')
  os.mkdir('compiled')

  for path in glob.glob('src/*.py'):
    with open(path) as f:
      text = f.read()

    subbed_text = sub_emojis(text)

    tree = ast.parse(subbed_text)

    class ConstantToEmoji(ast.NodeTransformer):
      def visit_Constant(self, node):
        node.value = emojis.encode(re.sub('_emoji_([a-z]+)_emoji_', ':\g<1>:', node.value))
        return node

    tree = ConstantToEmoji().visit(tree)
    compiled_text = astor.to_source(tree)

    original_filename = os.path.basename(path)
    for filename in original_filename, sub_emojis(original_filename):
      path2 = os.path.join('compiled', filename)
      with open(path2, 'w') as f:
        f.write(compiled_text)

def build_sub_emojis():
  emoji_to_real_name = {}

  def sub_emojis(text):
    compiled_text = text
    for emoji in emojis.get(text):
      if not emoji in emoji_to_real_name:
        emoji_to_real_name[emoji] = re.sub(':', '_emoji_', emojis.decode(emoji))
      compiled_text = re.sub(emoji, emoji_to_real_name[emoji], compiled_text)
    return compiled_text

  return sub_emojis
sub_emojis = build_sub_emojis()


if __name__ == '__main__':
  main()
