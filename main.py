import re
import pyperclip

text = '''               Python OOP Retake Exam - 23 August 2021










      '''  # <<<paste here

text = text.strip()
text_chars = re.sub("[:,!/?`.&'*-]", " ", text)
text_subfinal = re.sub('[ ]', '_', text_chars)
text_subfinal = text_subfinal.replace("__", "_")
text_final = text_subfinal.lower().strip()
pyperclip.copy(text_final)

spam = pyperclip.paste()
print(text_final)

# import pyperclip
# pyperclip.copy('The text to be copied to the clipboard.')
# spam = pyperclip.paste()
