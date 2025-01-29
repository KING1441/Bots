import tkinter as tk
import json

# Initiates and sets the window name
root = tk.Tk()
root.title("Game :)")

# Sets the window size
window_width = 600
window_height = 400

# Gets the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculates the center of your screen
center_x = int((screen_width - window_width) / 2)
center_y = int((screen_height - window_height) / 2)

# Creates the window in the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Creates a label
label = tk.Label(root, text="Deez")
label.place(x=150, y=50, width=300, height=50)

def on_entry_click(event):

    entry = event.widget

    if entry.get() == entry.placeholder:
        entry.delete(0, tk.END)
        entry.config(fg="black")

def on_focusout(event):

    entry = event.widget

    if entry.get() == "":
        entry.insert(0, entry.placeholder)
        entry.config(fg="grey")

def create_Entry(root, placeholder, x, y, width=300, height=30):
    entry = tk.Entry(root, fg="grey")
    entry.placeholder = placeholder
    entry.insert(0, placeholder)
    entry.bind('<FocusIn>', on_entry_click)
    entry.bind('<FocusOut>', on_focusout)
    entry.place(x=x, y=y, width=width, height=height)
    return entry

usernameBox = create_Entry(root, "Enter your username", 150, 200)
passwordBox = create_Entry(root, "Enter your password", 150, 250)

# Creates a button that register the data in the 'game.json' file
def register_data():

    username = usernameBox.get() if usernameBox.get() != usernameBox.placeholder else ""
    password = passwordBox.get() if passwordBox.get() != passwordBox.placeholder else ""

    print("Button clicked!")
    label.config(text="Get hacked L rizler")
    with open('game.json', 'r') as file:
        data = json.load(file)

    # Access the specified user's data
    
    data["data"]["users"][username] = {
        "username": username,    # Include username within the user data
        "password": password,
    }
    
    # Writes the data to the json file
    with open('game.json', 'w') as file:
        json.dump(data, file, indent=4)

# Checks if the button is clicked and calls the "register_data" function
button = tk.Button(root, text="Click Me", command=register_data)
button.place(x=150, y=150, width=300, height=50)


# Runs the code
root.mainloop()
