#DO NOT COPY THIS FILE!
#Anyone that wants to copy will need to pay to the Owner of This
from colorama import init, Fore
init()
Show = True
#Pazi = str(input("Say Anything: "))

#Class Printy
class PrintyTools:
    def Printy_Str(Text):
        if Show == True:
            print("You Used: Printy.Str")
        Text = str(Text)
        print(Text)

    def Printy_Math(Number1,Number2,m1):
        Number2 = Number2
        Number1 = Number1
        m1 = str(m1)
        Number1 = float(Number1)
        Number2 = float(Number2)
        if m1 == "+":
            if Show == True:
                print("Plus:")
            print(Number1+Number2)
        if m1 == "-":
            if Show == True:
                print("Minus:")
            print(Number1-Number2)
        if m1 == "/":
            if Show == True:
                print("Divided:")
            print(Number1/Number2)
        if m1 == "//":
            if Show == True:
                print("Divided Full Num:")
            print(Number1//Number2)
        if m1 == "%":
            if Show == True:
                print("Modulo:")
            print(Number1%Number2)

    def Printy():
        print("/n"*3)
        print(Fore.GREEN + "-----------------------------------")
        print(Fore.RED + "Printy Commands:")
        print(Fore.YELLOW + "- Printy()",Fore.CYAN + "[Call the Printy method to display all commands]")
        print(Fore.YELLOW + '- Printy_Math(Number1,Number2,"m1")',Fore.CYAN + "[Perform a math operation using Printy_Math method (e.g., addition of two numbers)]")
        print(Fore.YELLOW + '- Printy_Color("Text","color")',Fore.CYAN + "[Print text in a specific color using Printy_Color method]")
        print(Fore.YELLOW + '- Printy_Str("Text")',Fore.CYAN + "[Print a string using Printy_Str method (Normal Print)]")
        print(Fore.YELLOW + '- Printy_AllColors(True/False)',Fore.CYAN + "[Print all The Colors That You can use in Printy_Color]")
        print(Fore.RED + "Comming Soon...")
        print(Fore.RED + "Comming Soon...")
        print(Fore.GREEN + "-----------------------------------")
        print("")

    def Printy_Color(Text,color):
        Text = str(Text)
        color = str(color)
        Color = color.upper
        print(Color)
        if Show == True:
            print("Your'e using: Printy_Color")
        if Color == "RED":#
            print(Fore.RED + Text)
        if Color == "BLUE":#
            print(Fore.BLUE + Text)
        if Color == "GREEN":#
            print(Fore.GREEN + Text)
        if Color == "YELLOW":#
            print(Fore.YELLOW + Text)
        if Color == "MAGENTA":#
            print(Fore.MAGENTA + Text)
        if Color == "BLACK":#
            print(Fore.BLACK + Text)
        if Color == "WHITE":#
            print(Fore.WHITE + Text)
        if Color == "CYAN":#
            print(Fore.CYAN + Text)
        if Color == "LIGHTBLUE":#
            print(Fore.LIGHTBLUE_EX + Text)

    def Printy_AllColors(true):
        if true == False:
            print("")
        if true == True:
            print("All Colors: ",Fore.LIGHTBLUE_EX + "LIGHTBLUE",Fore.CYAN + "CYAN",Fore.WHITE + "WHITE",Fore.BLACK + "BLACK",Fore.MAGENTA + "MAGENTA",Fore.YELLOW + "YELLOW",Fore.BLUE + "BLUE",Fore.GREEN + "GREEN",Fore.RED + "RED")
#Code
PrintyTools.Printy_AllColors(True)

#from main import PrintyTools

    
