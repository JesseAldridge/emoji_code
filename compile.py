#!/usr/bin/env python3
import random, re, glob, os, shutil

import emojis


def main():
  shutil.rmtree('compiled')
  os.mkdir('compiled')

  for path in glob.glob('src/*.py'):
    with open(path) as f:
      text = f.read()

    emoji_to_real_name = {}
    compiled_text = text
    for emoji in emojis.get(text):
      emoji_to_real_name.setdefault(emoji, re.sub(':', '_', emojis.decode(emoji)))
      compiled_text = re.sub(emoji, emoji_to_real_name[emoji], compiled_text)

    filename = os.path.basename(path)
    path2 = os.path.join('compiled', filename)
    with open(path2, 'w') as f:
      f.write(compiled_text)

if __name__ == '__main__':
  main()
