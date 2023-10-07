from tkinter import Tk, Label, Text, Frame, Button, Entry, StringVar, OptionMenu
from googletrans import Translator, constants
from pathlib import Path
from PIL import ImageTk, Image
import pyperclip

Label_Font = ("Humnst777 Blk BT Black Italic", 15)
Text_Font = ("Berlin Sans FB", 15)

def translate(text):
    translated = Translator().translate(text, dest=constants.LANGCODES.get(Target.get()))
    textArea.set(translated.text)
        
    
window = Tk()
window.geometry("800x500")

window.config(bg="#0d1436")

textArea = StringVar()
Target = StringVar()
Options = list(constants.LANGUAGES.values())

frame = Frame(master=window, background="#080c20")
frame.pack(padx=40, pady=23, expand=True, fill="both")

label = Label(master=frame, text="Translator!", font=("Intro Rust G Base 2 Line", 20), bg="#080c20", foreground="#ffffff")
label.pack(padx=10, pady=10, anchor="n")

label = Label(master=frame, text="Insert Your Text:", font=Label_Font, bg="#080c20", foreground="#ffffff")
label.pack(padx=10, anchor="nw")

textbox = Entry(master=frame, border=0, width=55, font=Text_Font, textvariable=textArea, background="#0d1436", foreground="#ffffff")
textbox.pack(padx=10, pady=20, anchor="center")

copy_button = Button(master=frame, text="Copy", command=lambda: pyperclip.copy(textArea.get()))
copy_button.pack(padx=5, anchor="e")

label = Label(master=frame, text="Choose Language to translate to:", font=Label_Font, bg="#080c20", foreground="#ffffff")
label.pack(padx=10, anchor="nw")

Icon = ImageTk.PhotoImage(Image.open(Path(__file__).parent / "down.png").resize((50, 50)))

options = OptionMenu(frame, Target, *Options)
options.pack(padx=10, pady=5)
options.configure(background="#000000", foreground="#ffffff", image=Icon, indicatoron=False)

label = Label(master=frame, font=Label_Font, bg="#080c20", foreground="#ffffff", textvariable=Target)
label.pack(padx=10, before=options)

button = Button(master=frame, text="Translate", font=Label_Font, command=lambda: translate(textbox.get()))
button.pack(padx=10, pady=5, anchor="center")

window.mainloop()