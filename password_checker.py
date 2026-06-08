import re
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Hacker banner
banner = f"""{Fore.GREEN}

██████╗  █████╗ ███████╗███████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝███████║███████╗███████╗
██╔═══╝ ██╔══██║╚════██║╚════██║
██║     ██║  ██║███████║███████║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝

🔐 PASSWORD STRENGTH CHECKER
{Style.RESET_ALL}
"""

print(banner)

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    # Number check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    # Special character check
    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    # Strength result
    if score <= 2:
        strength = f"{Fore.RED}WEAK ❌"
    elif score <= 4:
        strength = f"{Fore.YELLOW}MEDIUM ⚠️"
    else:
        strength = f"{Fore.GREEN}STRONG ✅"

    return strength, suggestions


password = input(Fore.CYAN + "Enter your password: ")

strength, suggestions = check_password_strength(password)

print("\nPassword Strength:", strength)

if suggestions:
    print(Fore.MAGENTA + "\nSuggestions:")
    for s in suggestions:
        print(Fore.WHITE + f"➜ {s}")
else:
    print(Fore.GREEN + "\nExcellent password security!")
