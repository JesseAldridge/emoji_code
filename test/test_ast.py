import ast

text = '😆 = "😆"'

import pdb; pdb.set_trace()

ast.literal_eval(text)

# parsed = ast.parse(text)
# result = ast.dump(parsed, indent=2)
