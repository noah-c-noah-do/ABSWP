import pyperclip

text_list = ["*" + x for x in pyperclip.paste().split("\n")]
text = "\n".join(text_list)
pyperclip.copy(text)
