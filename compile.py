import random, re, glob, os

import emojis


def random_string():
  return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=4))

def main():
  if not os.path.exists('compiled'):
    os.mkdir('compiled')

  for path in glob.glob('src/*.py'):
    with open(path) as f:
      text = f.read()

    compiled_text = text
    for emoji in emojis.get(text):
      compiled_text = re.sub(emoji, random_string(), compiled_text)

    filename = os.path.basename(path)
    path2 = os.path.join('compiled', filename)
    with open(path2, 'w') as f:
      f.write(compiled_text)

if __name__ == '__main__':
  main()
