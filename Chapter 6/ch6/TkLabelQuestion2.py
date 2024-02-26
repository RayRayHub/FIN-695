#import the needed modules
import tkinter as tk

# create the root window
root = tk.Tk()
#specify the title and size of the root window
root.title("A Label Inside A Root Window")
root.geometry("850x160")
# create a label inside the root window
label = tk.Label(text="here is your label", fg="Red", font=("Helvetica", 80))
label.pack()
# run the game loop
root.mainloop()