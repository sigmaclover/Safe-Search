import pyperclip

while True:
    if "bad" in pyperclip.paste():
        pyperclip.copy("good")
