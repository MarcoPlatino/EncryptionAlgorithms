import CaeserCipher
import tkinter as tk

root = tk.Tk()
root.title("ROT# Encrypt/Decrypt")

# Variables
word1 = tk.StringVar()

# Defining all of the functions for all of the stuff aha
def encode():
    phrase = word1.get()
    encoded = CaeserCipher.encode(phrase, 10)
    answer1.config(text=encoded)


answer1 = tk.Label(root, text="No.")
answer1.pack()


firstWord = tk.Entry(root, textvariable=word1, font=('calibre', 10, 'bold'))
firstWord.pack()

process1 = tk.Button(root, text='Submit', command=encode)
process1.pack()

root.mainloop()
