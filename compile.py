#!/usr/bin/env python3
import random, re, glob, os, shutil

import emojis


def main():
  shutil.rmtree('compiled')
  os.mkdir('compiled')

  for path in glob.glob('src/*.py'):
    with open(path) as f:
      text = f.read()

    compiled_text = sub_emojis(text)
    filename = sub_emojis(os.path.basename(path))
    path2 = os.path.join('compiled', filename)
    with open(path2, 'w') as f:
      f.write(compiled_text)

def build_sub_emojis():
  emoji_to_real_name = {}

  def sub_emojis(text):
    compiled_text = text
    for emoji in emojis.get(text):
      if not emoji in emoji_to_real_name:
        emoji_to_real_name[emoji] = re.sub(':', '_', emojis.decode(emoji))
      compiled_text = re.sub(emoji, emoji_to_real_name[emoji], compiled_text)
    return compiled_text

  return sub_emojis
sub_emojis = build_sub_emojis()


if __name__ == '__main__':
  main()
