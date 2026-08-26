from termcolor import colored # pyrefly: ignore [missing-import]
import pyfiglet  # pyrefly: ignore [missing-import]


print(pyfiglet.figlet_format("Hello World"))
print(pyfiglet.figlet_format("PYTHON", font="slant"))
pyfiglet.figlet_format("HELLO", font="banner")
pyfiglet.figlet_format("HELLO", font="big")
pyfiglet.figlet_format("HELLO", font="doom")
pyfiglet.figlet_format("HELLO", font="slant")

text = pyfiglet.figlet_format("PYTHON")

print(colored(text, "cyan"))