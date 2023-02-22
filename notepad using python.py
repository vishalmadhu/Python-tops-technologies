from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

# Create a new window
root = Tk()
root.title("Untitled - Notepad")

# Create a text area
text_area = Text(root, font=("Arial", 12))
text_area.pack(expand=YES, fill=BOTH)

# Create a menu bar
menu_bar = Menu(root)

# Create the file menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=lambda: new_file())
file_menu.add_command(label="Open", command=lambda: open_file())
file_menu.add_command(label="Save", command=lambda: save_file())
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Set the menu bar
root.config(menu=menu_bar)

# Define the file functions
def new_file():
    # Clear the text area
    text_area.delete(1.0, END)
    # Update the title
    root.title("Untitled - Notepad")

def open_file():
    # Ask the user for a file to open
    file_path = askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        # Open the file
        with open(file_path, "r") as file:
            content = file.read()
        # Update the text area
        text_area.delete(1.0, END)
        text_area.insert(1.0, content)
        # Update the title
        root.title(f"{file_path} - Notepad")

def save_file():
    # Ask the user for a file name to save as
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        # Save the file
        with open(file_path, "w") as file:
            content = text_area.get(1.0, END)
            file.write(content)
        # Update the title
        root.title(f"{file_path} - Notepad")

# Start the main event loop
root.mainloop()
