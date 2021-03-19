import random, re, glob, os

import emojis


if not os.path.exists('compiled'):
  os.mkdir('compiled')

for path in glob.glob('src/*.py'):
  with open(path) as f:
    text = f.read()

  def random_string():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=4))

  emoji_to_real_name = {}
  compiled_text = text
  for emoji in emojis.get(text):
    emoji_to_real_name.setdefault(emoji, random_string())
    compiled_text = re.sub(emoji, emoji_to_real_name[emoji], compiled_text)

  filename = os.path.basename(path)
  path2 = os.path.join('compiled', filename)
  with open(path2, 'w') as f:
    f.write(compiled_text)
