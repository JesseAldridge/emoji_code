import re

import emojis

text = ':snake: _snake_ :asdf:'
print(emojis.encode(text))

print(re.sub('_emoji_([a-z]+)_emoji_$', ':\g<1>:', text))
