# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'

# Using the colors
print(f"{RED}This text is red!{RESET}")
print(f"{GREEN}This text is green!{RESET}")
print(f"{BLUE}This text is blue!{RESET}")

# Mixing colors
print(f"{YELLOW}Yellow text,{CYAN} followed by cyan,{MAGENTA} and then magenta.{RESET}")
print("Back to normal")

# Making the bell sound
print('\a')

