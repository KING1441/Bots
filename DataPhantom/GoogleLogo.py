import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Requires the Pillow library


def show_login_screen():
    """Display a Google-like login screen."""
    login_window = tk.Toplevel()  # Create a new window
    login_window.title("Login")
    login_window.geometry("400x400")
    login_window.configure(bg="white")

    # Google Logo
    try:
        logo_img = Image.open("googlelogo.png")
        logo_img = logo_img.resize((150, 50))  # Resize for the login screen
        logo_tk = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(login_window, image=logo_tk, bg="white")
        logo_label.image = logo_tk  # Keep a reference to avoid garbage collection
        logo_label.pack(pady=20)
    except FileNotFoundError:
        tk.Label(login_window, text="Google", font=("Arial", 24, "bold"), bg="white").pack(pady=20)

    # Welcome Text
    tk.Label(
        login_window,
        text="Sign in",
        font=("Arial", 20, "bold"),
        bg="white",
        fg="#202124",
    ).pack(pady=5)

    tk.Label(
        login_window,
        text="to continue to Google",
        font=("Arial", 12),
        bg="white",
        fg="#5f6368",
    ).pack()

    # Username Entry
    username_entry = tk.Entry(login_window, width=35, font=("Arial", 14), bg="#f1f3f4", bd=0)
    username_entry.pack(pady=20, padx=20)
    username_entry.insert(0, "Email or phone")
    username_entry.bind("<FocusIn>", lambda event: username_entry.delete(0, "end"))

    # Next Button
    def handle_next():
        if username_entry.get().strip() == "":
            messagebox.showerror("Error", "Enter an email or phone number")
        else:
            messagebox.showinfo("Next", f"Welcome, {username_entry.get()}!")

    tk.Button(
        login_window,
        text="Next",
        command=handle_next,
        font=("Arial", 12, "bold"),
        bg="#1a73e8",
        fg="white",
        bd=0,
        padx=20,
        pady=10,
        activebackground="#185abc",
        activeforeground="white",
    ).pack(pady=20)

    # Footer Links
    footer_frame = tk.Frame(login_window, bg="white")
    footer_frame.pack(side="bottom", pady=10)
    tk.Label(
        footer_frame, text="Help", font=("Arial", 10), fg="#1a73e8", bg="white", cursor="hand2"
    ).grid(row=0, column=0, padx=10)
    tk.Label(
        footer_frame, text="Privacy", font=("Arial", 10), fg="#1a73e8", bg="white", cursor="hand2"
    ).grid(row=0, column=1, padx=10)
    tk.Label(
        footer_frame, text="Terms", font=("Arial", 10), fg="#1a73e8", bg="white", cursor="hand2"
    ).grid(row=0, column=2, padx=10)


def display_google_logo():
    """Display the Google logo in a tkinter window."""
    root = tk.Tk()
    root.title("Google Logo in Tkinter")

    # Create a canvas
    canvas = tk.Canvas(root, width=600, height=400, bg="white")
    canvas.pack()

    # Load the Google logo
    try:
        img = Image.open("googlelogo.png")
        img = img.resize((400, 150))  # Resize the logo if necessary
        tk_image = ImageTk.PhotoImage(img)

        # Add the logo to the canvas and bind a click event
        logo = canvas.create_image(300, 200, image=tk_image, anchor="center")
        canvas.tag_bind(logo, "<Button-1>", lambda event: show_login_screen())
    except FileNotFoundError:
        print("Google logo file not found. Make sure 'googlelogo.png' is in the same directory as the script.")

    # Run the tkinter main loop
    root.mainloop()

# Call the function
display_google_logo()
