text = '😆 = f"{😆} 😆"'

compiled_chars = []
for ch in text:
  if ch == '"':
    compiled_chars.append(ch)
    state = IN_STRING
