from colorama import init, Fore
init()
Show = True
#Pazi = str(input("Say Anything: "))

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
    print(""*3)
    print(Fore.GREEN + "-----------------------------------")
    print(Fore.RED + "Printy Commands:")
    print(Fore.YELLOW + "- Printy()",Fore.CYAN + "[Shows A List Of All The Commands]")
    print(Fore.YELLOW + "- Printy_Math(Number1,Number2,m1)",Fore.CYAN + "[Enter 2 numbers and Change the m1 to the Thing you want to do]")
    print(Fore.YELLOW + "- Printy_Color(Text,color)",Fore.CYAN + "[Print With Colors]")
    print(Fore.YELLOW + "- Printy_Str(Text)",Fore.CYAN + "[Print In String (Normal Print)]")
    print(Fore.RED + "Comming Soon...")
    print(Fore.RED + "Comming Soon...")
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
    if color == "red":
        print(Fore.RED + Text)


Printy()
#Printy_Color("Red Text","red")
#Printy_Math(10,3,"%")
    
