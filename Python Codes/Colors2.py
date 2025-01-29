from colorama import init, Fore, Back, Style

# Initializes Colorama for Windows compatibility
init()

# Foreground colors (text colors)
print(Fore.RED + "Red")
print(Fore.BLUE + "BLUE")
print(Fore.YELLOW + "YELLOW")
print(Fore.GREEN + "GREEN")
print(Fore.MAGENTA + "MAGENTA")
print(Fore.BLACK + "BLACK")
print(Fore.CYAN + "CYAN")
print(Fore.WHITE + "WHITE")
print(Fore.LIGHTBLACK_EX + "LIGHTBLACK_EX")
print(Fore.LIGHTRED_EX + "LIGHTRED_EX")
print(Fore.LIGHTGREEN_EX + "LIGHTGREEN_EX")
print(Fore.LIGHTYELLOW_EX + "LIGHTYELLOW_EX")
print(Fore.LIGHTBLUE_EX + "LIGHTBLUE")
print(Fore.LIGHTMAGENTA_EX + "LIGHTMAGENTA_EX")
print(Fore.LIGHTCYAN_EX + "LIGHTCYAN_EX")
print(Fore.LIGHTWHITE_EX + "LIGHTWHITE_EX")

# Background colors (background colors for the text)
print(Back.RED + "Background Red")
print(Back.BLUE + "Background Blue")
print(Back.YELLOW + "Background Yellow")
print(Back.GREEN + "Background Green")
print(Back.MAGENTA + "Background Magenta")
print(Back.BLACK + "Background Black")
print(Back.CYAN + "Background Cyan")
print(Back.WHITE + "Background White")
print(Back.LIGHTBLACK_EX + "Background LIGHTBLACK_EX")

# Resetting background and text colors
print(Fore.RESET + Back.RESET + "Normal Text with Reset Background")

# Adding styles (bold, underlined, etc.)
print(Style.BRIGHT + "Bright Style Text")
print(Style.NORMAL + "Normal Style Text")
print(Style.DIM + "Dim Style Text")

# Combining Foreground, Background, and Style
print(Fore.YELLOW + Back.CYAN + Style.BRIGHT + "Bright Yellow on Cyan with Bold")

# Reset to default after each line
print(Fore.RESET + Back.RESET + Style.RESET_ALL + "Back to default")
