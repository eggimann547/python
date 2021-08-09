import random
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Password  \nGenerator")

print(ascii_banner)





lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWZYZ"
symbols = "!*"

all = lower + upper + symbols
length = 8
password = "".join(random.sample(all,length))
print(password)
