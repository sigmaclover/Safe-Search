import pyperclip

if "bad" in pyperclip.paste():
    print("You shouldn't do that")
    pyperclip.copy("good")

    print(pyperclip.paste())
else:
    print("all good")
