import os
import dsc_tools.future.ft_morph_rip
import db_menu
from dsc_tools.future.cursify import cursify
from dsc_tools.future.randomizer import MaxRandomizer
from tkinter import filedialog
import tkinter as tk
import main

if os.name == 'nt':
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')

def main():
    clear()
    print("????????????????????????????????????????????????????????????????????")
    print("? 1. Cursify DSC File                                              ?")
    print("? 2. Apply MAX Randomization to Chart (Caution, may be unplayable) ?")
    print("????????????????????????????????????????????????????????????????????")

    user_choice = input()

    if user_choice == "1":
        root = tk.Tk().withdraw()

        file_path = filedialog.askopenfilename(filetypes=[("Arcade/Future Tone/Mega39s DSC File", "*.dsc")])
        ext = os.path.splitext(file_path)
        with open(file_path, 'r+b') as f:
            with open(file_path + '.bak', 'wb') as bak:
                bak.write(f.read())
            dsc_tools.future.cursify.cursify(f)
            dsc_tools.future.cursify.cursify(f)

    if user_choice == "2":
        root = tk.Tk().withdraw()

        file_path = filedialog.askopenfilename(filetypes=[("Arcade/Future Tone/Mega39s DSC File", "*.dsc")])
        ext = os.path.splitext(file_path)
        with open(file_path, 'r+b') as f:
            with open(file_path + '.bak', 'wb') as bak:
                bak.write(f.read())
            dsc_tools.future.randomizer.MaxRandomizer(f)
            dsc_tools.future.randomizer.MaxRandomizer(f)
