import re
import pyperclip

text = '''                  09. Possible permutations










      '''  # <<<paste here

text = text.strip()
text_chars = re.sub("[:,!/?`.&'-]", " ", text)
text_subfinal = re.sub('[ ]', '_', text_chars)
text_subfinal = text_subfinal.replace("__", "_")
text_final = text_subfinal.lower().strip()
pyperclip.copy(text_final)

spam = pyperclip.paste()
print(text_final)

# import pyperclip
# pyperclip.copy('The text to be copied to the clipboard.')
# spam = pyperclip.paste()
